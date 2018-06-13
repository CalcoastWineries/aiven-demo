#!/usr/bin/env python
import sys
import time
# This script receives messages from a Kafka topic
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

#uri = "postgres://avnadmin:m3382yo5hlz9aopp@pg-19209ef7-freddyso-c424.aivencloud.com:11141/kafka-demo?sslmode=require"
uri = sys.argv[2]

db_conn = psycopg2.connect(uri)
c = db_conn.cursor(cursor_factory=RealDictCursor)

print ("Hello World! I am Kafka Consumer.")

while True:
  raw_msgs = consumer.poll(timeout_ms=1000)
  for tp, msgs in raw_msgs.items():
    for msg in msgs:
        print("I Received: {}".format(msg.value))
	c.execute("insert into authlog_messages (kafka_consumer, message) values ('demo_consumer','%s')" % (format(msg.value))) 
	db_conn.commit()
    print("I just committed the last few messages into PostgreSQL.")

