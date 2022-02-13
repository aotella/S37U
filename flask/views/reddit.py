from flask_restful import Resource
from flask import request, Response
from helper import reddit
from slack_sdk import WebClient
import json
import os


def create_slack_client():
    client = WebClient(token=os.environ.get("BOT_TOKEN"))
    return client


class PostRedditArticleOnSlack(Resource):
    def post(self):
        request_data = request.json
        client = create_slack_client()
        return_data = reddit.update_post(client, request_data)
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)
        else:
            return Response(json.dumps(return_data), status=400)
