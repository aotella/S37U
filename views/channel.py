from flask_restful import Resource
from flask import request, Response
import json

class UpsertChannel(Resource):
    def post(self):
        request_data = request.json
        if request_data is None:
            return Response("Bad Request", status=400)
        return_data = {"status":"success"} #Add return from function
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)

        else:
            return Response(json.dumps(return_data), status=400)


class GetChannelKeyword(Resource):
    def get(self, channel_id):
        print(channel_id)
        return_data = {"status":"success"} #Add return from function
        if return_data["status"] == "success":
            return Response(json.dumps(return_data), status=200)
        else:
            return Response(json.dumps(return_data), status=400)