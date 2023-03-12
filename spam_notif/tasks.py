from __future__ import absolute_import, unicode_literals

from celery import shared_task
import os
from slack import WebClient
from slack.errors import SlackApiError

@shared_task
def send_alert(payload,slack_token,channel_name):

    client = WebClient(token=slack_token)

    blocks = [
        {
        'type':'header',
         "text": {
				"type": "plain_text",
				"text": f'{payload["Name"]} :tada:' ,
				"emoji": True
			}
        },
        {
			"type": "divider",
		},
        {
        'type':'section',
        "fields": [
				{
					"type": "mrkdwn",
					"text": f"*Email:*\n {payload['Email']}"
				},
        ]
        },
        {
			"type": "divider",
		},
        {
        'type':'section',
        "fields": [
				{
					"type": "mrkdwn",
					"text": f"*Description:*\n {payload['Description']}"
				},
        ]
        },
        {
			"type": "divider",
		},
    ]

    client.chat_postMessage(channel=channel_name, blocks=blocks)