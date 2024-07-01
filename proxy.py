from dotenv import load_dotenv
import websocket
import json
import os
import requests
from apprise import Apprise, AppriseConfig

load_dotenv()

gotify_host = os.environ['GOTIFY_HOST']
gotify_token = os.environ['GOTIFY_TOKEN']
apprise_config = os.environ['APPRISE_CONFIG'] if 'APPRISE_CONFIG' in os.environ else '/config/apprise.conf'

config = AppriseConfig()
config.add(f"file://{apprise_config}")

apprise = Apprise()
apprise.add(config)

def on_message(ws, message):
    msg = json.loads(message)
    apprise.notify(
        body=msg['title'],
        title=msg['message'],
    )

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("Connection closed")

def on_open(ws):
    print("Opened Gotify websocket connection")

if __name__ == "__main__":
    wsapp = websocket.WebSocketApp("ws://" + str(gotify_host) + "/stream", header={"X-Gotify-Key": str(gotify_token)},
                                   on_open=on_open,
                                   on_message=on_message,
                                   on_error=on_error,
                                   on_close=on_close)
    wsapp.run_forever()