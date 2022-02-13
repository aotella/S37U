# S37U

Introducing Bob!

Bob is the slack bot to get micro-communities to flourish in your company. :seedling: Say bye to boredom, transactional work and isolation! Say hello to smooth onboarding, colleagues with rapport and proactive and tight knit communities! :100:

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
