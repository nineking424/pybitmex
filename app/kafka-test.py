from producer import MessageProducer
import sys
import threading
import os
import time
from log import get_logger

logger = get_logger('kafka-test')
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
        logger.info(str(e))
        print("Failed to initialize Kafka producer. Exiting...")
        sys.exit(1)

if __name__ == "__main__":

    init_kafka("TEST")
    res = message_producer.send_message("START : " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
    logger.info(res)
