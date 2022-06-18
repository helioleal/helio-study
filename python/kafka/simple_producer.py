'''
When kafka is up, this program
produce 5 messages and send to kafka broker for topic impacta_project
Taken from: https://kafka-python.readthedocs.io/en/master/
'''
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
for i in range(5):
    producer.send('impacta_project', b'msg %d' % i)
producer.flush()
