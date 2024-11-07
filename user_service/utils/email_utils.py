from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType

from user_service.settings import settings

config = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_SENDER,
    MAIL_SERVER=settings.MAIL_HOST,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
)


async def send_email(email_body: str, receiver_email: str) -> None:
    message = MessageSchema(
        subject="Welcome to our service!",
        recipients=[receiver_email],
        body=email_body,
        subtype=MessageType.plain
    )
    mail = FastMail(config=config)
    await mail.send_message(message)
