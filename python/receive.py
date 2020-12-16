#!/usr/bin/env python
import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='ihtiandr9.fvds.ru'))
    channel = connection.channel()

    channel.queue_declare(queue='glass',durable=True)
    #channel.queue_declare(queue='rpc_queue')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())

    #channel.basic_consume(queue='rpc_queue', on_message_callback=callback, auto_ack=True)
    channel.basic_consume(queue='glass', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
