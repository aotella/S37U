from flask_restful import Resource
from flask import request, Response
from helper import channel_invite, channel_keywords, interests
from slack_sdk import WebClient
import json
import os


def create_slack_client():
    client = WebClient(token=os.environ.get("BOT_TOKEN"))
    return client


class UpsertChannelKeywords(Resource):

    '''
    
    endpoint :- /api/v1/channel/
    expected input :- {"channel_id": "","keywords": [""]}
    Updates channel with keyword provided in the request.
    
    '''

    def post(self):
        request_data = request.json
        return_data = channel_keywords.update_channel_info(request_data)
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)

        else:
            return Response(json.dumps(return_data), status=400)


class GetChannelKeyword(Resource):

    '''
    
    endpoint :- "/api/v1/channel/<string:channel_id>"
    expected input :- channel_id
    Return all the channel ids for that particular keywords.
    
    '''

    def get(self, channel_id):
        return_data = channel_keywords.get_channel_info(channel_id)
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)
        else:
            return Response(json.dumps(return_data), status=400)

class AddUserToChannel(Resource):


    '''
    
    endpoint :- "/api/v1/channel/add/"
    expected input :- {"interests": [""],"user_id": ""}
    Based on interests, sends notification to all channel associated to them to add the user.
    
    '''

    def post(self):
        request_data = request.json
        client = create_slack_client()
        return_data = channel_invite.send_channel_invitation(client, request_data)
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)
        else:
            return Response(json.dumps(return_data), status=400)


class GetAllChannelInfo(Resource):


    '''
    
    endpoint :- "/api/v1/channelkeyword/"
    expected input :- 
    Return all the channels in db with name, keywords and subreddits associated.
    
    '''

    def get(self):
        return_data = channel_keywords.get_all_channel_info()
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)
        else:
            return Response(json.dumps(return_data), status=400)


class GetChannelByInterests(Resource):

    '''
    
    endpoint :- "/api/v1/interestchannel/<string:interest>"
    expected input :- interest
    Based on interest returns all the channel. 
    
    '''


    def get(self, interest):
        return_data = interests.get_channels_by_interest(interest)
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)
        else:
            return Response(json.dumps(return_data), status=400)


class UpdateChannelForInterests(Resource):


    '''

    endpoint :- "/api/v1/interestchannel/"
    expected input :- {"channels" : [""],"interest": ""}
    Adds channel to interests [In case new channel is created for a domain in that interest.]

    '''
    def post(self):
        request_data = request.json
        return_data = interests.update_channel_for_interest(request_data)
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)
        else:
            return Response(json.dumps(return_data), status=400)
