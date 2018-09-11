import pika
import json

from config import Config

parameters = pika.ConnectionParameters(Config.RABBIT_MQ_SERVER)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='provisioning')

channel.basic_publish(exchange='', routing_key='provisioning', body="starting up...")

def publish(msg):
    channel.basic_publish(exchange='', routing_key='provisioning', body=json.dumps(msg))
