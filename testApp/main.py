import os
from Google import Create_Service
import pandas as pd

API_NAME = 'photoslibrary'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = 'creds.json'
SCOPES = [
    'https://www.googleapis.com/auth/photoslibrary',
    'https://www.googleapis.com/auth/photoslibrary.sharing',

]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_NAME, SCOPES)

print(dir(service))
