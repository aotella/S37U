from flask_restful import Resource
from flask import request, Response
from helper import channel_ranking
from slack_sdk import WebClient
import json
import os


def create_slack_client():
    client = WebClient(token=os.environ.get("BOT_TOKEN"))
    return client


class GetChannelRanking(Resource):
    def get(self):
        client = create_slack_client()
        return_data = channel_ranking.return_channel_ranking(client)
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)
        else:
            return Response(json.dumps(return_data), status=400)
