from helper import send_message
import logging
import json

logger = logging.getLogger(__name__)

def get_channel_keywords_info():
    with open('common/keywords.json') as f:
        channel_data = json.loads(f.read())
    return channel_data

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

    channel_data = get_channel_keywords_info()
    print(channel_data)
    return {"status": "success", "data": channel_data}


def get_channel_info(channel_id):


    channel_keyword_map = get_channel_keywords_info().get(channel_id, "")

    if channel_keyword_map == "":
        return{"status": "failure", "message": "keyword not found"}

    return {"status": "success", "data": channel_keyword_map}


def update_channel_info(request_data):

    
    channel_keyword_map = get_channel_keywords_info()

    try:
        channel_id = request_data["channel_id"]
        keywords = request_data["keywords"]
    except Exception as e:
        logger.info(e)
        return {"status": "failure", "message": "incorrect request"}

    channel_keyword_map[channel_id]["keywords"] = keywords

    if update_channel_keywords(channel_keyword_map):
        channel_keyword_map = get_channel_keywords_info()
        return {"status": "success", "data": channel_keyword_map[channel_id]}

    else:
        return {"status": "success", "data": channel_keyword_map}