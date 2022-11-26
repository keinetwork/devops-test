import pika
import json

params = pika.URLParameters('amqps://hlvjquvf:kY5awSPhgzrMre23Gi4ziZCS7uC1txwg@dingo.rmq.cloudamqp.com/hlvjquvf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='order',body=json.dumps(body),properties=properties)