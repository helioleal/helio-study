## This script create a new topic on Kafka

* 1 - Open your CMD
* 2 - Go to Kafka folder
* 3 - Type the following command:
```
C:\kafka\bin\windows>kafka-topics.bat --create --bootstrap-server 192.168.0.86:9092 --topic topiconovo
	Created topic topiconovo.
```
* 4 - This command just created a new topic on Kafka called "topiconovo"
* 5 - To see available topics on Kafka type
```
C:\kafka\bin\windows>kafka-topics.bat --bootstrap-server 192.168.0.86:9092 --describe
Topic: topiconovo       TopicId: zZr990bIRAaAZy_okT45DQ PartitionCount: 1       ReplicationFactor: 1    Configs: segment.bytes=1073741824
        Topic: topiconovo       Partition: 0    Leader: 0       Replicas: 0     Isr: 0
```
