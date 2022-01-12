import os

from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# from slacker import Slacker # 2021.2.24일 이후 생성 계정은 SLAKCER 안됨 - webclient 이용해야 한다

load_dotenv()
SLACK_TOKEN = os.getenv("SLACK_TOKEN")


def send_slack_message(channel, message):
    client = WebClient(token=SLACK_TOKEN)
    try:
        res = client.chat_postMessage(channel=channel, text=message)
        return res
    except SlackApiError as e:
        print(f"Got an Error :: {e.response['error']}")
