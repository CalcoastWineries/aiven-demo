#!/usr/bin/env python
import sys
import time
# This script receives messages from a Kafka topic
from kafka import KafkaConsumer

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

print ("Hello World!")

raw_msgs = consumer.poll(timeout_ms=1000)
for tp, msgs in raw_msgs.items():
    for msg in msgs:
        print("Received: {}".format(msg.value))

