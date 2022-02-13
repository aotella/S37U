import logging
import json

logger = logging.getLogger(__name__)


def return_channels_of_user(client, user_id):

    try:
        next_cursor = "1"
        channel_ids = []
        while next_cursor != "":
            result = client.users_conversations(
                user=user_id,
            ).data
            for channels in result["channels"]:
                if channels["is_channel"] == True:
                    channel_ids.append(channels['id'])

            next_cursor = result["response_metadata"]["next_cursor"]
        return channel_ids
    except Exception as e:
        logger.error(e)
        return []