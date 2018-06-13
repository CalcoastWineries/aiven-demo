CREATE TABLE authlog_messages(
 kafka_consumer VARCHAR (50) NOT NULL,
 message TEXT NOT NULL,
 created_on TIMESTAMP without time zone DEFAULT timestamp 'now ( )' NOT
NULL
);
