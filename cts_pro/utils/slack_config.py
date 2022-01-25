import logging
import os

from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.web import client

# from slacker import Slacker # 2021.2.24일 이후 생성 계정은 SLAKCER 안됨 - webclient 이용해야 한다
# class refactoring

logger = logging.getLogger(__name__)
load_dotenv()
SLACK_TOKEN = os.getenv("SLACK_TOKEN")
print(SLACK_TOKEN)


class SlackBot:
    def __init__(self) -> None:
        self.client = WebClient(token=os.getenv("SLACK_TOKEN"))

    def send_slack_message(self, channel, message):
        try:
            res = self.client.chat_postMessage(channel=channel, text=message)
            return res
        except SlackApiError as e:
            print(f"Got an Error :: {e.response['error']}")

    def get_channel_id(self, channel_name):
        """
        conversations_list() 메서드 호출 => channel_id get
        """
        try:
            result = self.client.conversations_list()
            # 슬랙봇 권한문제 설정해줘야 됨
            # 채널 정보 딕셔너리 리스트
            channels = result.data["channels"]
            print(channels)
            # 채널 명이 'test'인 채널 딕셔너리 쿼리
            # 람다 함수 수정 필요
            channel = list(filter(lambda c: c["name"] == channel_name, channels))[0]
            # 채널ID 파싱
            channel_id = channel["id"]
            return channel_id
        except SlackApiError as e:
            logger.error(f"get_channel_id error | msg {e}")

    def get_message_ts(self, channel_id, query):
        """
        슬랙 채널 내 메세지 조회
        """
        try:
            # conversations_history() 메서드 호출
            result = client.conversations_history(channel=channel_id)
            # 채널 내 메세지 정보 딕셔너리 리스트
            messages = result.data["messages"]
            # 채널 내 메세지가 query와 일치하는 메세지 딕셔너리 쿼리
            message = list(filter(lambda m: m["text"] == query, messages))[0]
            # 해당 메세지ts 파싱
            message_ts = message["ts"]
            return message_ts
        except SlackApiError as e:
            logger.error(f"get_message_ts error | msg {e}")

    def get_channel_members(self, channel_id):
        try:
            result = self.client.conversations_members(channel=channel_id, limit=100)
            return result
        except SlackApiError as e:
            logger.error(f"Error Slack_api get channel members | error message ::{e}")

    def send_direct_message(self, members):
        try:
            i = 0
            print(len(members["members"]))
            while i < len(members["members"]):
                print(i, end="  ")
                result = self.client.chat_postMessage(
                    channel=members["members"][i],
                    blocks=[
                        {
                            "type": "section",
                            "fields": [
                                {"type": "mrkdwn", "text": "*Type:*\nPaid Time Off"},
                                {
                                    "type": "mrkdwn",
                                    "text": "*Created by:*\n<example.com|Fred Enriquez>",
                                },
                            ],
                        },
                        {
                            "type": "section",
                            "fields": [
                                {"type": "mrkdwn", "text": "*When:*\nAug 10 - Aug 13"}
                            ],
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": "<https://example.com|View request>",
                            },
                        },
                    ],
                )
                logger.info(result)
                print("result dm :::::", result)
                i += 1
            return "Succes send to DM"
        except SlackApiError as e:
            logger.error(f"Error Slack_api send dm | error message ::{e}")


if __name__ == "__main__":
    res = SlackBot()
    asb = res.get_channel_id(channel_name="테스팅")
    print(asb)
    memebers = res.get_channel_members(channel_id=asb)
    print(memebers)
    dm = res.send_direct_message(members=memebers)
    print(dm)
