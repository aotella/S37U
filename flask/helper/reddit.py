from asyncio.log import logger
from re import sub
from site import execsitecustomize
from helper import send_message
import praw
import os
import json
import random
from models import Channel

CLIENT_ID=os.environ["CLIENT_ID"]
CLIENT_SECRET=os.environ["CLIENT_SECRET"]
USER_AGENT=os.environ["USER_AGENT"]


def get_subreddits_by_channel(channel_id):

    print(channel_id)
    channel_subreddits = Channel.objects(channel_id=channel_id).first().to_json()
    print(type(channel_subreddits))

    print(channel_subreddits["subreddits"])

    return channel_subreddits["subreddits"]

    # with open('common/keywords.json') as f:
    #     channel_data = json.loads(f.read())
    # return channel_data[channel]["subreddits"]


def get_reddit_post(subreddit):


    post_data = {}
    reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)
    top_posts = reddit.subreddit(subreddit).hot(limit=1)
    for post in top_posts:
        print(post)
        post_data["post_url"] = post.url
        post_data["post_title"] = post.title

    return post_data


def update_post(client, request_json):

    channel_id = request_json.get("channel_id", "")

    subreddit_list = get_subreddits_by_channel(channel_id)

    if subreddit_list != []:
        subreddit_data = random.choice(subreddit_list)
        post_data = get_reddit_post(subreddit_data)

    else:
        return {"status": "failure", "message": "no subreddit present"}

    try:
        send_message.send_message(client, channel_id, "post", post_data)
        return {"status": "success", "channel_id": channel_id, "post": post_data}
    except Exception as e:
        logger.error(e)
        return {"status": "failure", "message": "message not posted"}