import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


logger = logging.getLogger(__name__)


def get_user_with_similar_interest(user_id):


    channel_id = request_json.get("channel_id", "")

    subreddit_list = get_subreddits_by_channel(channel_id)

    subreddit_data = random.choice(subreddit_list)

    post_data = get_reddit_post(subreddit_data)

    try:
        send_message.send_message(client, channel_id, "post", post_data)
        return {"status": "success", "channel_id": channel_id, "post": post_data}
    except Exception as e:
        logger.info(e)
        return {"status": "failure", "message": "message not posted"}