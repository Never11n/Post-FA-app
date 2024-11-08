import pika
import json


def publish_to_queue(email: str, username: str) -> None:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='send_email')

    message = json.dumps({"email": email, "username": username})
    channel.basic_publish(exchange='', routing_key='send_email', body=message)
    connection.close()
