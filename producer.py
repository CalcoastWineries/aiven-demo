#!/usr/bin/env python
import sys
import time
# This script connects to Kafka and send a few messages 
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=sys.argv[1],
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)

print ("Hello World!  I am Kafka Producer.")

def follow(thefile):
  thefile.seek(0,2)
  while True:
    line = thefile.readline()
    if not line:
      time.sleep(0.1)
      continue
    yield line

if __name__ == '__main__':
  logfile = open('/var/log/auth.log', 'r')
  loglines = follow(logfile)
  for line in loglines:
#    print ('do something here')
#    print (line)

    print("I am Sending: {}".format(line))
    producer.send("auth.log", line.encode("utf-8"))

# Wait for all messages to be sent

    producer.flush()
