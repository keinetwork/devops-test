import pika
import os, django
from user_order.models import Order, Shop

os.environ.setdefault("DJANGO_SETTINGS_MODEL", 'order.settings')
django.setup()

params = pika.URLParameters('amqps://hlvjquvf:kY5awSPhgzrMre23Gi4ziZCS7uC1txwg@dingo.rmq.cloudamqp.com/hlvjquvf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='order')

def callback(ch, method, properties, body):
    print('Received in order')
    id = json.loads(body)
    print(id)
    order = Order.objects.get(id=id)
    order.deliver_finish = 1
    order.save()
    print('order deliver finished')

channel.basic_consume(queue='order', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()