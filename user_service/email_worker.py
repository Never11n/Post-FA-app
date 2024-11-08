import json

import pika

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


async def send_email(username: str, receiver_email: str) -> None:
    message = MessageSchema(
        subject="Welcome to our service!",
        recipients=[receiver_email],
        body=f'{username}, welcome to our service',
        subtype=MessageType.plain
    )
    mail = FastMail(config=config)
    await mail.send_message(message)


def callback(ch, method, properties, body):
    data = json.loads(body)
    send_email(receiver_email=data["email"], username=data["username"])


def start_worker():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='send_email')
    channel.basic_consume(queue='send_email', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == "__main__":
    start_worker()
