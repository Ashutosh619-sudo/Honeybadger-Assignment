from .tasks import send_alert
import os

def send_slack_alert(payload):

    slack_token = os.environ.get("SLACKTOKEN")
    channel_name = os.environ.get("CHANNELNAME")
    
    send_alert.delay(payload,slack_token,channel_name)