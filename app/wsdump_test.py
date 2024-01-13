import websocket
import _thread
import time
import rel
import json
from producer import MessageProducer

message_producer=None
BOOTSTRAP_SERVERS='kafka-broker:9094'

def on_message(ws, msg):
    print(msg)
    res=message_producer.send_message(msg)
    # print(res)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")

def init_kafka(topic):
    global message_producer
    message_producer = MessageProducer(BOOTSTRAP_SERVERS, topic)
    
if __name__ == "__main__":

    # init kafka producer
    init_kafka('test-topic')

    # init websocket
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://api.gemini.com/v1/marketdata/BTCUSD",
    # ws = websocket.WebSocketApp("wss://ws.bitmex.com/realtime?subscribe=trade:XBTUSD",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()