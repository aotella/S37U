from S37U.helper import send_message
import logging

logger = logging.getLogger(__name__)

def get_channel_id(channel_name):
    pass


def send_channel_invitation(client, request_json):

    channel_id = request_json.get("channel_id", "")
    channel_name = request_json.get("channel_name", "")
    user_name = request_json.get("user_name")

    if channel_id != "":
        pass
    elif channel_id == "" and channel_name != "":
        channel_id = get_channel_id(channel_name)
    else:
        return {"status": "failure", "message": "provide channel_id or channel_name", "status_code": 400}

    message = f"Hi <!channel>,  <@{user_name}> wants to join your channel please invite them and greet them."
    print(channel_id, user_name, message)

    try:
        result = send_message.send_message(client, channel_id, "message", message)
        print(result)
        logger.info(result)
        return {"status": "success"} 
    except Exception as e:
        logger.info(e)
        return {"status": "failure"} 