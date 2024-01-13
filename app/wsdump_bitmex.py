import websocket
import time
import rel
import json
from producer import MessageProducer
import sys
import threading

INTERVAL_SECONDS = 5
BOOTSTRAP_SERVERS='kafka-broker:9094'

message_producer=None
last_received_time=0

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

def healthcheck():
    global last_received_time
    current_time = time.time()
    elapsed_time = current_time - last_received_time if last_received_time else 0
    print("Time elapsed since last message:", elapsed_time)
    if elapsed_time > INTERVAL_SECONDS:
        print("Sent ping")
        send_websocket_message(ws, "ping")
        last_received_time=current_time

def on_message(ws, msg):
    global last_received_time
    last_received_time = time.time()
    
    # print(msg)
    res = message_producer.send_message(msg)
    # print(res)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")
    set_interval(healthcheck, INTERVAL_SECONDS)

def init_kafka(topic):
    global message_producer
    message_producer = MessageProducer(BOOTSTRAP_SERVERS, topic)

def send_websocket_message(ws, message):
    ws.send(message)

    
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python wsdump_bitmex.py <subscribe>")
        sys.exit(1)

    subscribe=sys.argv[1]
    print("subscribe: ", subscribe)

    # init kafka producer
    init_kafka(subscribe.replace(":", "."))
    # init websocket
    ws = websocket.WebSocketApp("wss://ws.bitmex.com/realtime?subscribe="+subscribe,
    # ws = websocket.WebSocketApp("wss://ws.bitmex.com/realtime?subscribe=instrument:XBTUSD",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()
# python3 wsdump_bitmex.py instrument:XBTUSD
# python3 wsdump_bitmex.py trade:XBTUSD