#!/bin/bash

#It is assumed that the user has Zookeeper, Kafka installed in the default locations

echo "Starting Zookeeper..."
nohup zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties > zookeeper.log 2>&1 &

sleep 5

echo "Starting Kafka Server..."
nohup kafka-server-start /usr/local/etc/kafka/server.properties > kafka.log 2>&1 &


sleep 5

echo "Running Python scripts..."
python3 server.py > server.log 2>&1 &
python3 prod.py > prod.log 2>&1 &

echo "All services have been started"
