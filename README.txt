This exercise is done using Aiven Kafka Service and Aiven Postgresql Service

Assumption: Only a single system is used for this exercise.  The system is configured with python 2.7.9 or above with python modules: psycopg2 and kafka-python.  In addition, postgresql-client is installed on the system.

producer.py - listen for new entries from /var/log/auth.log, whenever a new entry is discovered, it would rewrite the same entry as a message into the auth.log topic of Kafka

consuser.py - listen for new message from auth.log topic of Kafka, and it will rewrite the message as text datatype into postgresql database where the database name is kafka-demo and the tablename is authlog_messages.

kafka-demo.sql - to be used to create the table authlog_messages

Setup:

On the Aiven Service Cnsole, create an Aiven Kafka Service and then create "auth.log" topic,
Note that the SSL certificate files from the Aiven Kafka Servie just created.  They needed to be downloaded by clicking the "Show CA certificate" as ca.pem, "Show access certificate" as service.cert and "Show access key buttons" as service.key.  Record the service url for running both the producer.py and the consumer.py.

    e.g. "kafka-32fe272c-freddyso-c424.aivencloud.com:11143"
    
Again, on the Aiven Service Cnsole, create an Aiven PostgreSQL Service and then create database kafka-demo.  Record the service url for running the consumer.py.  

    e.g. "postgres://avnadmin:m3382yo5hlz9aopp@pg-19209ef7-freddyso-c424.aivencloud.com:11141/kafka-demo?sslmode=require"

On the testing system CLI, create table using kafta-demo.sql with the PostgreSQL client
  
    e.g. vagrant@vagrant:~$ psql postgres://avnadmin:m3382yo5hlz9aopp@pg-19209ef7-freddyso-c424.aivencloud.com:11141/kafka-demo?sslmode=require < kafka-demo.sql
  
To run the producer, pass in the kafka service URL
    e.g. vagrant@vagrant:~$ ./producer.py "kafka-32fe272c-freddyso-c424.aivencloud.com:11143"
  
To run the consusmer, pass in both the kafka and the postgresql service URL
    e.g. vagrant@vagrant:~$ ./consumer.py "kafka-32fe272c-freddyso-c424.aivencloud.com:11143" "postgres://avnadmin:m3382yo5hlz9aopp@pg-19209ef7-freddyso-c424.aivencloud.com:11141/kafka-demo?sslmode=require"

Testing:
On the system where the producer.py and consumer.py is running, simply login and logoff with new session or run any sudo command. 
    e.g. 'sudo lsb_release -a'

Observe that the console output where producer.py is ruuning and the console output where consumer.py is running.  The new entries printed on both console would match.  In addiion, new table rows would match the new entries as well as soon as the database commit is indicated on the console where consumer.py is running.
