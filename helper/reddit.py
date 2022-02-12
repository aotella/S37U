import praw
CLIENT_ID="Ag8Z4R8JjkMZyJn5Ip5IFQ"
CLIENT_SECRET="0Klw_0qpO_tVYUhpsN1Z21Q0PnRaQQ"
USER_AGENT="s37u-slack"


def get_reddit_post(subreddit):


    post_data = {}
    reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)
    top_posts = reddit.subreddit(subreddit).top(limit=1)
    for post in top_posts:
        post_data["post_url"] = post.url
        post_data["post_title"] = post.title

    return post_data