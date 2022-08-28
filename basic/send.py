# establish a connection with the rabbitmq server

import pika

# using a broker on the local machine (localhost)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# declare a queue to receive messages
channel.queue_declare(queue='hello')

#  ready to start sending messages
# routing key specifies the queue to receive messages
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='PRINCE IS A PLAYER'
)

print('message sent to hello queue')
# close the connection
connection.close()
