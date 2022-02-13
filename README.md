# S37U

Introducing Bob!

Bob is the slack bot to get micro-communities to flourish in your company. :seedling: Say bye to boredom, transactional work and isolation! Say hello to smooth onboarding, colleagues with rapport and proactive and tight knit communities! :100:

Bob - The community bot that keeps companies engaged & happening! :handshake:

Building culture, a tight knit workplace and rapport among colleagues can be difficult, especially in the WFH world!

Bob allows companies to manage micro communities or interest groups with ease and keep the conversation going - fostering communication :loud_sound:  rapport building :handshake:  & engagement among employees.

**Onboard employees into the office culture & interest groups that allow teammates to bond outside of work!**

1. Get employee interests and add them to groups  :heart_eyes:
2. Set tags or keywords to groups to enable community discovery :hash:
3. Inform groups and ask them to assimilate newbies into the group with warm welcomes! :pray:

**Micro-community engagement**

1. Starts conversations by automatically and periodically sharing articles on trending hashtags related to a community
2. Send customized prompts for communities to get users talking! :speech_balloon:
3. Keep track of community activation - recognize & reward the most active communities in your org! :trophy:


Try Bob today to make the workplace more than just a workplace but a community of likeminded individuals!

## Steps to run Bob! 

It takes two apps, node and flask to get Bob up and running

### Node

#### Go to `node` directory

`cd node`

#### Install dependencies

`npm install`

#### Run the app

`node app.js`

### Flask

#### Create a virtual environment

`python -m venv .venv`

#### Source into virtual environment

`source .venv/bin/activate`

#### Install packages

`pip install -r requirements.txt`

#### Start server

`gunicorn -b 0.0.0.0:5001 wsgi:app`
