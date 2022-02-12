from flask_restful import Resource
from flask import request, Response
from S37U.helper import channel_invite, channel_keywords, interests
from slack_sdk import WebClient
import json
import os


def create_slack_client():
    client = WebClient(token=os.environ.get("BOT_TOKEN"))
    return client


class UpsertChannelKeywords(Resource):
    def post(self):
        request_data = request.json
        return_data = channel_keywords.update_channel_info(request_data)
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)

        else:
            return Response(json.dumps(return_data), status=400)


class GetChannelKeyword(Resource):
    def get(self, channel_id):
        return_data = channel_keywords.get_channel_info(channel_id) 
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)
        else:
            return Response(json.dumps(return_data), status=400)


class GetAllKeywords(Resource):
    def get(self):
        return_data = channel_keywords.get_all_channel_info() 
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)
        else:
            return Response(json.dumps(return_data), status=400)


class AddUserToChannel(Resource):
    def post(self):
        request_data = request.json
        client = create_slack_client()
        return_data = channel_invite.send_channel_invitation(client, request_data)
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)
        else:
            return Response(json.dumps(return_data), status=400)


class GetAllChannelInfo(Resource):
    def get(self):
        return_data = channel_keywords.get_all_channel_info()
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)
        else:
            return Response(json.dumps(return_data), status=400)



class GetChannelByInterests(Resource):
    def get(self, interest):
        return_data = interests.get_channels_by_interest(interest)
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)
        else:
            return Response(json.dumps(return_data), status=400)