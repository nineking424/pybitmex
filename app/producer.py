from kafka import KafkaProducer
import json
import time
from csv import reader


class MessageProducer:
    broker = ""
    producer = None
    topic = ""

    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=self.broker,
                                    #   value_serializer=lambda x: json.dumps(x).encode('utf-8'),
                                      value_serializer=lambda x: x.encode('utf-8'),
                                      acks=0,
                                      retries=3
                                      )

    def send_message(self, msg):
        try:
            future = self.producer.send(self.topic, msg)
            self.producer.flush()   # 비우는 작업
            future.get(timeout=5)
            return {'status_code': 200, 'error': None}
        except Exception as e:
            print("error:::::",e)
            return e

    def send_message_async(self, msg):
        try:
            future = self.producer.send(self.topic, msg)
            return {'status_code': 200, 'error': None}
        except Exception as e:
            return e
if __name__ == '__main__':
    # 브로커와 토픽명을 지정한다.
    broker = '192.168.1.5:9094'
    topic = 'new-topic'
    message_producer = MessageProducer(broker, topic)

    with open('test/'+topic+'.txt', 'r', encoding='utf-8') as file:
        for data in file:
            print("send-data: ", data)
            res = message_producer.send_message(topic, data)