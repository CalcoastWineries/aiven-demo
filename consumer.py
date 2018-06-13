#!/usr/bin/env python
import sys
import time
from kafka import KafkaConsumer
from psycopg2.extras import RealDictCursor
import psycopg2

consumer = KafkaConsumer(
    "auth.log",
    bootstrap_servers=sys.argv[1],
    client_id="demo-client-1",
    group_id="demo-group",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)

# setup postgresql db connecdtion
uri = sys.argv[2]

db_conn = psycopg2.connect(uri)
c = db_conn.cursor(cursor_factory=RealDictCursor)

print ("Hello World! I am Kafka Consumer.")

# receiveing messages from a Kafka topic
# insert messages into postgresql
while True:
  raw_msgs = consumer.poll(timeout_ms=1000)
  for tp, msgs in raw_msgs.items():
    for msg in msgs:
        print("I Received: {}".format(msg.value))
	c.execute("insert into authlog_messages (kafka_consumer, message) values ('demo_consumer','%s')" % (format(msg.value))) 
	db_conn.commit()
    print("I just committed the last few messages into PostgreSQL.")

