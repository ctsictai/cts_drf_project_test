import os

from dotenv import load_dotenv
from slacker import Slacker

load_dotenv()
SLACK_TOKEN = os.getenv("SLACK_TOKEN")


def slack_notify(channel, message):
    try:
        slack = Slacker(SLACK_TOKEN)
        slack.chat.post_message(channel, message)
    except Exception as e:
        print(e)
