from flask import Flask, render_template
from flask_restful import Api, Resource
from S37U.views import channel, interest

app = Flask(__name__)

# two decorators, same function
api = Api(app)

api.add_resource(channel.UpsertChannelKeywords, '/api/v1/channel/')
api.add_resource(channel.GetAllChannelInfo, '/api/v1/channelkeyword/')
api.add_resource(channel.GetChannelKeyword, '/api/v1/channel/<string:channel_id>')
api.add_resource(channel.AddUserToChannel, '/api/v1/channel/add/')
api.add_resource(interest.GetUserInterest, '/api/v1/userinterest/<string:user_id>')
api.add_resource(interest.UpdateUserInterest, '/api/v1/userinterest/')
api.add_resource(channel.GetChannelByInterests, '/api/v1/interestchannel/<string:interest>')



if __name__ == "__main__":
    app.run(host="0.0.0.0")