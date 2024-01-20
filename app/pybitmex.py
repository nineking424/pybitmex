import websocket
import time
import rel
from producer import MessageProducer
import sys
import threading
import os

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
last_received_time=0
ws = None
url = WEBSOCKET_URL + SUBSCRIBE

def set_interval(func, interval):
    """
    Calls the given function repeatedly with the specified interval.

    Parameters:
    func (function): The function to be called.
    interval (float): The time interval between function calls in seconds.
    """
    def wrapper():
        func()
        threading.Timer(interval, wrapper).start()
    wrapper()

def on_message(ws, msg):
    global last_received_time
    last_received_time = time.time()
    
    # print(msg) # For debugging
    res = message_producer.send_message(msg)
    # print(res) # For debuggingSUBSCRIBE

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")
    set_interval(healthcheck, INTERVAL_SECONDS)

def init_kafka(topic):
    global message_producer
    try:
        message_producer = MessageProducer(BOOTSTRAP_SERVERS, topic)
    except Exception as e:
        print(str(e))
        print("Failed to initialize Kafka producer. Exiting...")
        sys.exit(1)

def init_websocket():
    global ws
    # init websocket
    try:
        ws = websocket.WebSocketApp(url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

        ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    except Exception as e:
        print(str(e))
        print("Failed to initialize websocket. Exiting...")
        sys.exit(1)

def send_websocket_message(ws, message):
    ws.send(message)

def healthcheck():
    global last_received_time
    current_time = time.time()
    elapsed_time = current_time - last_received_time if last_received_time else 0
    print("Time elapsed since last message:", elapsed_time)
    if elapsed_time > INTERVAL_SECONDS:
        try:
            print("Sent ping")
            send_websocket_message(ws, "ping")
        except Exception as e:
            print("Failed to send ping. Exiting...")
            sys.exit(1)

if __name__ == "__main__":

    print("INTERVAL_SECONDS: ", INTERVAL_SECONDS)
    print("BOOTSTRAP_SERVERS: ", BOOTSTRAP_SERVERS)
    print("WEBSOCKET_URL: ", WEBSOCKET_URL)
    print("SUBSCRIBE: ", SUBSCRIBE)

    # init kafka producer
    init_kafka(SUBSCRIBE.replace(":", "."))
    init_websocket()
# python3 pybitmex.py