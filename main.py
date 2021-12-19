from slack_sdk import WebClient

token = 'xoxb-2873001082209-2860360577010-5TO5dyOLkO6jC2owSqeSXzAC'

class SlackAPI:
    def __init__(self, token):
        self.client = WebClient(token)

    def get_channel_id(self, channel_name):
        result = self.client.conversations_list()
        channels = result.data['channels']
        # 채널명이 channel_name과 같은 채널의 딕셔너리 가져오기
        channel = list(filter(lambda c: c['name'] == channel_name, channels))[0]
        # 채널 id 파싱
        channel_id = channel['id']
        return channel_id

    def get_message_ts(self, channel_id, query):
        """
        슬랙 채널 내 메시지 조회
        """
        result = self.client.conversations_history(channel=channel_id)
        messages = result.data['messages']
        message = list(filter(lambda m: m['text'] == query, messages))[0]
        message_ts = message['ts']
        return message_ts

    def post_thread_message(self, channel_id, message_ts, text):
        """
        슬랙채널 내 메세지의 thread에 댓글달기
        """
        result = self.client.chat_postMessage(
            channel=channel_id,
            text=text,
            thread_ts=message_ts
        )
        return result


slack = SlackAPI(token)
channel_name = "슬랙봇-테스트"
query = "테스트 메시지"
text = "Hello World"

channel_id = slack.get_channel_id(channel_name)
message_ts = slack.get_message_ts(channel_id, query)
# 댓글달기
slack.post_thread_message(channel_id, message_ts, text)
