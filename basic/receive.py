import pika
import sys
import os


def main():
    """consumer: consumes messages from queue """
    # establish connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    # declare  queue
    channel.queue_declare(queue='hello')

    # callback to run when a message is received
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    # consume message
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


# keep program running in a never ending loop until keyboard interrupt
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(1)
