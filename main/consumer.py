from os import environ

import pika

hostname = environ.get('RABBIT_HOST') or 'rabbitmq'
port = environ.get('RABBIT_PORT') or 5672

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=hostname, port=port,
        heartbeat=3600, blocked_connection_timeout=3600
    )
)

channel = connection.channel()
channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Start consuming')

channel.start_consuming()


channel.close()
