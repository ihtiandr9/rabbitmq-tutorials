#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='ihtiandr9.fvds.ru'))
channel = connection.channel()

channel.queue_declare(queue='glass',durable=True)

for i in range(5000):
    channel.basic_publish(exchange='', routing_key='glass', body='Hello World! %s '% i)
    print(" [x] Sent 'Hello World!' %s times" % i)
connection.close()
