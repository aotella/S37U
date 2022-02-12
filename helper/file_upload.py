import logging
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
def file_upload(client, channel_id, file_name):
# The name of the file you're going to upload
file_name = "./myFileName.gif"
# ID of channel that you want to upload file to

try:
    # Call the files.upload method using the WebClient
    # Uploading files requires the `files:write` scope
    result = client.files_upload(
        channels=channel_id,
        initial_comment="Here's my file :smile:",
        file=file_name,
    )
    # Log the result
    logger.info(result)

except SlackApiError as e:
    logger.error("Error uploading file: {}".format(e))