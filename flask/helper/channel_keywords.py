from helper import send_message
import logging
import json
from models import Channel

logger = logging.getLogger(__name__)

def get_channel_keywords_info():

    pass

    # with open('common/keywords.json') as f:
    #     channel_data = json.loads(f.read())
    # return channel_data

def update_channel_keywords(keyword_data):
    try:
        with open('common/keywords.json', 'w') as f:
            f.write(json.dumps(keyword_data))
        return 1
    except Exception as e:
        logger.info(e)
        return 0


def get_channel_keywords_info_db(channel_name):
    pass



def get_all_channel_info():

    channel_data = json.loads(Channel.objects().to_json())
    return {"status": "success", "data": channel_data}

    # channel_data = get_channel_keywords_info()
    # return {"status": "success", "data": channel_data}


def get_channel_info(channel_id):


    channel_data = Channel.objects(channel_id=channel_id).first().to_json()
    if channel_data is not None:
        return {"status": "success", "data": channel_data}
    else:
        return {{"status": "failure", "data": "channel not found"}}

    # channel_keyword_map = get_channel_keywords_info().get(channel_id, "")

    # print(channel_keyword_map)

    # if channel_keyword_map == "":
    #     return{"status": "failure", "message": "keyword not found"}

    # 


def return_channel_name(channel_id):
    from slack_sdk import WebClient
    import os 
    client = WebClient(token=os.environ.get("BOT_TOKEN"))

    channel_name = client.conversations_info(
        channel=channel_id
    ).data["channel"]["name"]
    return channel_name



def update_channel_info(request_data):
    try:
        channel_id = request_data["channel_id"]
        keywords = request_data["keywords"]
    except Exception as e:
        logger.info(e)
        return {"status": "failure", "message": "incorrect request"}

    try:
        channel = Channel.objects(channel_id=channel_id).first()
        if channel is None:
            channel_name = return_channel_name(channel_id)
            channel_obj = Channel(
                channel_id = channel_id,
                channel_name = channel_name, 
                keywords = keywords,
                subreddits = []
            )
            channel_obj.save()
            return {"status": "success", "data": json.loads(channel_obj.to_json())}

        
        else:
            channel.update(keywords=keywords)
            return {"status": "success", "data": json.loads(channel.to_json())}
    except Exception as e:
        logger.info(e)
        return {"status": "failure", "data": "keyword not updated"}


    # channel_keyword_map = get_channel_keywords_info()

    # try:
    #     channel_id = request_data["channel_id"]
    #     keywords = request_data["keywords"]
    # except Exception as e:
    #     logger.info(e)
    #     return {"status": "failure", "message": "incorrect request"}
    # channel_key = channel_keyword_map.get(channel_id, "")

    # if channel_key == "":
    #     from slack_sdk import WebClient
    #     import os 
    #     channel_keyword_map[channel_id]  = {}
    #     channel_keyword_map[channel_id]["keywords"] = keywords
    #     channel_keyword_map[channel_id]["subreddits"] = []

    #     client = WebClient(token=os.environ.get("BOT_TOKEN"))

    #     channel_name = client.conversations_info(
    #         channel=channel_id
    #     ).data["channel"]["name"]

    #     channel_keyword_map[channel_id]["channel_name"] = channel_name

    # channel_keyword_map[channel_id]["keywords"] = keywords

    # if update_channel_keywords(channel_keyword_map):
    #     channel_keyword_map = get_channel_keywords_info()
    #     return {"status": "success", "data": channel_keyword_map[channel_id]}

    # else:
    #     return {"status": "success", "data": channel_keyword_map}