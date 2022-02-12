from asyncio.log import logger
import json
from urllib.parse import uses_fragment

def get_interest_data():
    with open('S37U/common/interest-user.json') as f:
        interest_data = json.loads(f.read())
    return interest_data


def update_interest_data(interest_data):
    try:
        with open('S37U/common/interest-user.json', 'w') as f:
            f.write(json.dumps(interest_data))
        return 1
    except Exception as e:
        logger.info(e)
        return 0

def update_interests(request_json):

    interest_data = get_interest_data()

    user_id = request_json["user_id"]
    interests = request_json["interests"]

    if interests == []:
        return {"status": "error", "message": "interest list empty"}

    interest_data[user_id] = interests

    if update_interest_data(interest_data):
        interest_data = get_interest_data()
        return {"status": "success", "data": interest_data[user_id]}

    else:
        return {"status": "failure", "message": "update failed"}



def get_interests(user_id):

    interest_data = get_interest_data()
    users_interest = interest_data.get(user_id, "")

    if users_interest == "":
        return {"status": "failure", "message": "user not found"}
    else:
        return {"status": "success", "data": users_interest}


def get_channels_by_interest(interest):

    with open('S37U/common/interest.json') as f:
        interest_data = json.loads(f.read())


    if interest_data == "":
        return{"status": "failure", "message": "keyword not found"}

    return {"status": "success", "data": interest_data[interest]}