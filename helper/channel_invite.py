from S37U.helper import send_message
import logging
import json

logger = logging.getLogger(__name__)

def get_channel_id(channel_name):
    pass


def get_channel_id_by_interest(channel_keyword):
    with open('S37U/common/interest.json') as f:
        channel_data = json.loads(f.read())
    print(channel_data[channel_keyword])
    return channel_data[channel_keyword]["channel_id"]

def send_channel_invitation(client, request_json):

    channel_id_list = []
    interests = request_json.get("interests", "")
    user_id = request_json.get("user_id", "")
    for interest in interests:
        channel_id_list = channel_id_list + get_channel_id_by_interest(interest)

    try:
        for channel_id in channel_id_list:
            message = f"Hi <!channel>,  <@{user_id}> wants to join your channel please invite them and greet them."
            result = send_message.send_message(client, channel_id, "message", message)
            logger.info(result)
        return {"status": "success"} 
    except Exception as e:
        logger.info(e)
        return {"status": "failure"} 