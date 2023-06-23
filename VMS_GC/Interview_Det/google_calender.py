import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from django.http import request

SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_credentials():
    credentials = None
    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file(
            'token.json', SCOPES)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'D:\Django\Framework\VMS_GC\Interview_Det\Credentials.json', SCOPES)
            credentials = flow.run_local_server(port=0)

        # Save the credentials to a JSON file
        with open('token.json', 'w') as token_file:
            token_file.write(credentials.to_json())

    return credentials
