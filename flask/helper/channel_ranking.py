from helper import send_message
import json
import time
import logging
from models import Channel
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
import json


logger = logging.getLogger(__name__)


def get_channel_list():

    try:
        return_data = []
        channel_list = json.loads(Channel.objects().only("channel_id").to_json())
        for channel in channel_list:
            return_data.append(channel["channel_id"])
        return return_data
    except Exception as e:
        logger.error(e)
        return []


def get_message_count(client, channel_id):

    try:
        result = client.conversations_history(
            channel=channel_id, oldest=str(time.time() - 259200)
        )
        count = len(result.data["messages"])
        return count
    except SlackApiError as e:
        logger.error(e)
        return 0


def return_channel_ranking(request_data):

    client = WebClient(token=os.environ.get("BOT_TOKEN"))

    try:
        channel_list = get_channel_list()
        ranking_data = []
        for channel in channel_list:
            ranking_data.append(
                {"channel_id": channel, "count": get_message_count(client, channel)}
            )
        ranking_data = sorted(ranking_data, key=lambda i: i["count"], reverse=True)
        return {"status": "success", "data": ranking_data}
    except Exception as e:
        logger.error(e)
        return {"status": "failure", "message": "ranking not available"}
