import os 
from flask_mongoengine import MongoEngine


DB_URI = os.environ['DB_URI']
db = MongoEngine()



class User(db.Document):
    user_id = db.StringField()
    interests = db.ListField()
    def to_json(self):
        return {"user_id": self.user_id,
                "interests": self.interests}


class Channel(db.Document):
    channel_id = db.StringField()
    channel_name = db.StringField()
    keywords = db.ListField()
    subreddits = db.ListField()
    def to_json(self):
        return {"channel_id": self.channel_id,
                "channel_name": self.channel_name,
                "keywords": self.keywords, 
                "subreddits": self.subreddits
                }

class Interests(db.Document):
    interest = db.StringField()
    channels = db.ListField()
    def to_json(self):
        return {"interest": self.interest,
                "channels": self.channels, 
                }