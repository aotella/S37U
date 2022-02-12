from flask_restful import Resource
from flask import request, Response
from S37U.helper import channel_invite, channel_keywords, interests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json
import os


def create_slack_client():
    client = WebClient(token=os.environ.get("BOT_TOKEN"))
    return client




class UpsertChannel(Resource):
    def post(self):
        request_data = request.json
        if request_data is None:
            return Response("Bad Request", status=400)
        return_data = {"status":"success"} 
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



class AddUserToChannel(Resource):
    def post(self):
        request_data = request.json
        client = create_slack_client()
        return_data = channel_invite.send_channel_invitation(client, request_data)
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)
        else:
            return Response(json.dumps(return_data), status=400)



class GetUserInterest(Resource):
    def get(self, user_id):
        return_data = interests.get_interests(user_id)
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)
        else:
            return Response(json.dumps(return_data), status=400)


class UpdateUserInterest(Resource):
    def post(self):
        request_data = request.json
        return_data = interests.update_interests(request_data)
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)
        else:
            return Response(json.dumps(return_data), status=400)
