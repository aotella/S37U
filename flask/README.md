# S37U

## Setup

#### Create a virtual environment

`python -m venv .venv`

#### Source into virtual environment

`source .venv/bin/activate`

#### Install packages

`pip install -r requirements.txt`

#### Start server

`gunicorn -b 0.0.0.0:8000 wsgi:app`
