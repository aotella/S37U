from S37U.helper import send_message
import logging
import json

logger = logging.getLogger(__name__)

def get_channel_keywords_info(channel_keyword):
    with open('S37U/common/invite.json') as f:
        channel_data = json.loads(f.read())

    
    return channel_data.get(channel_keyword, "")


def get_channel_keywords_info_db(channel_name):
    pass



def get_channel_info(channel_keyword):


    channel_keyword_map = get_channel_keywords_info(channel_keyword)

    if channel_keyword_map == "":
        return{"status": "failure", "message": "keyword not found"}

    return {"status": "success", "data": channel_keyword_map}