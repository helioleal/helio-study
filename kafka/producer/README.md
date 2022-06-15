## This script createas a new producer via cmd

* 1 - Open your CMD
* 2 - Go to kafka folder
* 3 - Type the following command: 
```
C:\kafka\bin\windows>kafka-console-producer.bat --broker-list localhost:9092 --topic topiconovo
```
* 4 - topiconovo is the name of your topic.
* 5 - Press enter, you will be on producer console
* 6 - Then, type your messages, for example:
```
line0,550
line1,330
line2,5899
```
* 7 - These messages are been sent to topico 'topiconovo'
