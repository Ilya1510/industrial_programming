#!/usr/bin/env python
import pika
import time
import random

conn_params = pika.ConnectionParameters('rabbit', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='first-queue')

random_value = random.randint(0, 1000)
for i in range(20):
    channel.basic_publish(exchange='',
			  routing_key='first-queue',
			  body=str(random.randint(0, random_value)))
    print("Greeting sent")
    time.sleep(2)
print("generated value = " + str(random_value))
connection.close()
