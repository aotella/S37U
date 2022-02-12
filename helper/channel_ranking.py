from S37U.helper import send_message
import json
import time
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os


logger = logging.getLogger(__name__)

logger = logging.getLogger(__name__)

def get_channel_list():
    with open('S37U/common/channel_list.json') as f:
        channel_data = json.loads(f.read())
    return channel_data["channel_list"]


def get_channel_keywords_info_db(channel_name):
    pass



def get_message_count(client, channel_id):

    try:
        result = client.conversations_history(channel=channel_id, oldest=str(time.time()-259200))
        count = len(result.data["messages"])
        return count
    except SlackApiError as e:
        return 0
        pass




def return_channel_ranking(request_data):

    client = WebClient(token=os.environ.get("BOT_TOKEN"))
    try:
        channel_list = get_channel_list()
        ranking_data = []
        for channel in channel_list:
            ranking_data.append({"channel_id": channel, "count": get_message_count(client, channel)})
        ranking_data = (sorted(ranking_data, key = lambda i: i['count'], reverse=True))[:3]
        return {"status": "success", "data": ranking_data}
    except Exception as e:
        logger.info(e)
        return {"status": "failure", "message": "ranking not available"}
