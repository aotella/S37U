import praw
import os
CLIENT_ID=os.environ["CLIENT_ID"]
CLIENT_SECRET=os.environ["CLIENT_SECRET"]
USER_AGENT=os.environ["USER_AGENT"]


def get_reddit_post(subreddit):


    post_data = {}
    reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)
    top_posts = reddit.subreddit(subreddit).top(limit=1)
    for post in top_posts:
        post_data["post_url"] = post.url
        post_data["post_title"] = post.title

    return post_data