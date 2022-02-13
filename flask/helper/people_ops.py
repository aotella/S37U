import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


logger = logging.getLogger(__name__)


def get_user_with_similar_interest(user_id):

    try:
        send_message.send_message(client, channel_id, "post", post_data)
        return {"status": "success", "channel_id": channel_id, "post": post_data}
    except Exception as e:
        logger.error(e)
        return {"status": "failure", "message": "message not posted"}