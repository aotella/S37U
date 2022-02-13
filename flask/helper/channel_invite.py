from helper import send_message, member_check
import logging
import json
from models import Interests

logger = logging.getLogger(__name__)

def get_channel_id(channel_name):
    pass


def get_channel_id_by_interest(channel_keyword):

    interests = Interests.objects(interest=channel_keyword).first().to_json()
    return interests["channels"]

    # with open('common/interest-channel.json') as f:
    #     channel_data = json.loads(f.read())
    # return channel_data[channel_keyword]["channel_ids"]

def send_channel_invitation(client, request_json):

    channel_id_list = []
    interests = request_json.get("interests", "")
    user_id = request_json.get("user_id", "")
    for interest in interests:
        channel_id_list = channel_id_list + get_channel_id_by_interest(interest)
    users_channel = member_check.return_channels_of_user(client, user_id)
    try:
        for channel_id in channel_id_list:
            if channel_id in users_channel:
                print("user already in channel")
                pass
            else:
                message = f"Hi <!channel>,  <@{user_id}> wants to join your channel please invite them and greet them."
                result = send_message.send_message(client, channel_id, "message", message)
                logger.info(result)
        return {"status": "success"} 
    except Exception as e:
        logger.error(e)
        return {"status": "failure"} 