from flask import Flask, render_template
from flask_restful import Api, Resource
from views import channel, interest, reddit, ranking
import os
from models import db, DB_URI


app = Flask(__name__)

# two decorators, same function
api = Api(app)

app.config["MONGODB_HOST"] = DB_URI


db.init_app(app)
api.add_resource(channel.UpsertChannelKeywords, "/api/v1/channel/")  # Done
api.add_resource(channel.GetAllChannelInfo, "/api/v1/channelkeyword/")  # Done
api.add_resource(
    channel.GetChannelKeyword, "/api/v1/channel/<string:channel_id>"
)  # Done
api.add_resource(channel.AddUserToChannel, "/api/v1/channel/add/")  # Done

# ------------

api.add_resource(
    interest.GetUserInterest, "/api/v1/userinterest/<string:user_id>"
)  # Done
api.add_resource(interest.UpdateUserInterest, "/api/v1/userinterest/")  # Done
api.add_resource(
    channel.GetChannelByInterests, "/api/v1/interestchannel/<string:interest>"
)
api.add_resource(reddit.PostRedditArticleOnSlack, "/api/v1/redditpost/")  # Done
api.add_resource(ranking.GetChannelRanking, "/api/v1/ranking/")  # done
api.add_resource(channel.UpdateChannelForInterests, "/api/v1/interestchannel/")  # done


if __name__ == "__main__":
    app.run(host="0.0.0.0")
