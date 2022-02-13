from flask_restful import Resource
from flask import request, Response
from helper import interests
import json


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
