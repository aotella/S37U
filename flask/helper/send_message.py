import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


logger = logging.getLogger(__name__)


def send_message(client, channel_id, msg_type, message):
    try:
        result = None
        # Call the chat.postMessage method using the WebClient
        if msg_type == "post":
            post_title = message["post_title"]
            post_url = message["post_url"]
            result = client.chat_postMessage(
                channel=channel_id, text=f"{post_title}\n{post_url}"
            )
        if msg_type == "message":
            result = client.chat_postMessage(channel=channel_id, text=f"{message}")
        logger.info(result)
        return result

    except SlackApiError as e:
        logger.error(f"Error posting message: {e}")
