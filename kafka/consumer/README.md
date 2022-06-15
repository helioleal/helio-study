## Consume Kafka messages

* 1 - Open your CMD
* 2 - Go to Kafka folder
* 3 - Type the following command:
```
kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic topiconovo
```
* 4 - You will see that nothing will happen, this is because it is listening to messages who is comming from now on.
* 5 - If you open other CMD and produce new messages, this consumer will listen this new messages. Attention that can be a delay on messages.
* 6 - If you want to listen to message who has passed, use the following:
```
kafka-console-consumer.bat --bootstrap-server 192.168.0.86:9092 --topic topiconovo --from-beginning
```
