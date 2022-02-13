import logging
import json
from models import User, Interests

logger = logging.getLogger(__name__)

# def get_interest_data():
#     with open('common/interest-user.json') as f:
#         interest_data = json.loads(f.read())
#     return interest_data


# def update_interest_data(interest_data):
#     try:
#         with open('common/interest-user.json', 'w') as f:
#             f.write(json.dumps(interest_data))
#         return 1
#     except Exception as e:
#         logger.error(e)
#         return 0


def update_interests(request_json):

    # interest_data = get_interest_data()

    user_id = request_json["user_id"]
    interests = request_json["interests"]

    if interests == []:
        return {"status": "error", "message": "interest list empty"}

    try:
        user_obj = User.objects(user_id=user_id).first()

        if not user_obj:
            user = User(user_id=user_id, interests=interests)
            user.save()
            return {"status": "success", "data": user.to_json()}
        else:
            user_obj.update(interests=interests)
            return {"status": "success", "data": request_json}
    except Exception as e:
        logger.error(e)
        return {"status": "failure", "message": "not updated"}


def get_interests(user_id):

    try:
        user_obj = User.objects(user_id=user_id).first()

        if not user_obj:
            return {"status": "failure", "message": "user not found"}

        users_interest = user_obj.to_json()["interests"]
        return {"status": "success", "data": users_interest}

    except Exception as e:
        logger.error(e)
        return {"status": "failure", "message": "not updated"}


def get_channels_by_interest(interest):

    try:
        interest_obj = Interests.objects(interest=interest)

        if not interest_obj:
            return {"status": "failure", "message": "keyword not found"}

        interest_data = json.loads(interest_obj.to_json())

        return {"status": "success", "data": interest_data}

    except Exception as e:
        logger.error(e)
        return {"status": "failure", "message": "something went wrong"}

    # with open('common/interest-channel.json') as f:
    #     interest_data = json.loads(f.read())

    # if interest_data == "":
    #     return{"status": "failure", "message": "keyword not found"}

    # return {"status": "success", "data": interest_data[interest]}


def update_channel_for_interest(request_json):

    try:
        interest = request_json["interest"]
        channel_ids = request_json["channels"]

        channel_obj = Interests.objects(interest=interest).first()

        channels_for_interest = channel_obj.channels

        new_interest_list = list(set(channels_for_interest).union(set(channel_ids)))
        channel_obj.update(channels=new_interest_list)
        return {"status": "success"}

    except Exception as e:
        logger.error(e)
        return {"status": "failure"}
