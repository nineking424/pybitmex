from producer import MessageProducer
import sys
import threading
import os
import time

## dotenv
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv(override=False)
INTERVAL_SECONDS=int(os.environ.get('INTERVAL_SECONDS'))
BOOTSTRAP_SERVERS=os.environ.get('BOOTSTRAP_SERVERS')
WEBSOCKET_URL=os.environ.get('WEBSOCKET_URL')
SUBSCRIBE=os.environ.get('SUBSCRIBE')

# Global variables
message_producer=None

def init_kafka(topic):
    global message_producer
    try:
        message_producer = MessageProducer(BOOTSTRAP_SERVERS, topic)
    except Exception as e:
        print(str(e))
        print("Failed to initialize Kafka producer. Exiting...")
        sys.exit(1)

if __name__ == "__main__":

    print("INTERVAL_SECONDS: ", INTERVAL_SECONDS)
    print("BOOTSTRAP_SERVERS: ", BOOTSTRAP_SERVERS)
    print("WEBSOCKET_URL: ", WEBSOCKET_URL)
    print("SUBSCRIBE: ", SUBSCRIBE)

    init_kafka(SUBSCRIBE.replace(":", "."))
    res = message_producer.send_message("START : " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
    print(res)
