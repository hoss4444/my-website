import os
import json
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

# 1. Setup the "Robot User" (Service Account)
# This pulls the long JSON key you put in GitHub Secrets
service_account_info = json.loads(os.environ.get('GDRIVE_SERVICE_ACCOUNT_KEY'))
creds = service_account.Credentials.from_service_account_info(service_account_info)
service = build('drive', 'v3', credentials=creds)

# 2. Find your Excel File
# Replace 'YOUR_FILE_ID_HERE' with the ID from your Google Drive link
FILE_ID = 'YOUR_FILE_ID_HERE' 
request = service.files().get_media(fileId=FILE_ID)
file_stream = io.BytesIO()
downloader = MediaIoBaseDownload(file_stream, request)

done = False
while done is False:
    status, done = downloader.next_chunk()

# 3. Convert Excel to JSON for your Website
file_stream.seek(0)
df = pd.read_excel(file_stream)
# This saves the data as 'data.json' which your HTML will use
df.to_json('data.json', orient='records')
print("Successfully updated data.json!")
