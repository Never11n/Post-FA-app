from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

from post_service.settings import settings
from post_service.schemas import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


async def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = str(payload.get("user_id"))
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(id=user_id)
    except JWTError:
        raise credentials_exception

    return token_data


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    token = await verify_access_token(token, credentials_exception)
    return token.id
