This exercise is done using Aiven Kafka Service and Aiven Postgresql Service

Assumption: Only a single system is used for this exercisei. It is already configured with python 2.7.9 or above, and python modules: psycopg2 and kafka-python.
Also, postgresql-client is already installed

producer.py - listen for new entries from /var/log/auth.log, whenever a new entry is discovered, it would rewrite the same entry in to the auth.log topic

Note also that the Kafka SSL certificate files referred to in the scripts need to be downloaded from the Aiven Kafka Service view by clicking the Show CA certificate, Show access certificate and Show access key buttons.

It requires the Kafka Service URL passed in as parameter

e.g.
vagrant@vagrant:~$ ./producer.py "kafka-32fe272c-freddyso-c424.aivencloud.com:11143"

consuser.py - listen for new message from auth.log topic, and it will rewrite teh message as text datatype into postgresql database.  database name = kafka-demo, table name = authlog_messages

It requires the Kafka Service URL and the PostgreSQL Service URL passed in as parameters

e.g.
vagrant@vagrant:~$ ./consumer.py "kafka-32fe272c-freddyso-c424.aivencloud.com:11143" "postgres://avnadmin:m3382yo5hlz9aopp@pg-19209ef7-freddyso-c424.aivencloud.com:11141/kafka-demo?sslmode=require"

Testing:

On Aiven Service Cnsole
Create an Aiven Kafka Service
Create auth.log topic in Kafka
Create an Aiven PostgreSQL Service
Create database kafka-demo

create table using kafta-demo.sql
e.g.
vagrant@vagrant:~$ psql postgres://avnadmin:m3382yo5hlz9aopp@pg-19209ef7-freddyso-c424.aivencloud.com:11141/kafka-demo?sslmode=require < kafka-demo.sql

On the host where the producer.py is running, simply login and logoff with new session or run any sudo command e.g. 'sudo lsb_release -a'

