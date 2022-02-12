from flask import Flask, render_template
from flask_restful import Api, Resource
from S37U.views import channel

app = Flask(__name__)

# two decorators, same function
api = Api(app)

api.add_resource(channel.UpsertChannel, '/api/v1/channel/')
api.add_resource(channel.GetChannelKeyword, '/api/v1/channel/<string:channel_id>')
api.add_resource(channel.AddUserToChannel, '/api/v1/channel/add/')
api.add_resource(channel.GetUserInterest, '/api/v1/userinterest/<string:user_id>')
api.add_resource(channel.UpdateUserInterest, '/api/v1/userinterest/')

if __name__ == "__main__":
    app.run(host="0.0.0.0")