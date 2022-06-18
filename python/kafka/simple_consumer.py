'''
When kafka is online in local server, this program consumes everything
from a topic called impacta_project
Taken from: https://kafka-python.readthedocs.io/en/master/ 
'''
from kafka import KafkaConsumer

consumer = KafkaConsumer('impacta_project')
for msg in consumer:
    print (msg)