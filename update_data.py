import os
import json
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

# 1. Setup the "Robot User" (Service Account)
service_account_info = json.loads(os.environ.get('GDRIVE_SERVICE_ACCOUNT_KEY'))
creds = service_account.Credentials.from_service_account_info(service_account_info)
service = build('drive', 'v3', credentials=creds)

# 2. List all your Excel Files here
FILES_TO_SYNC = {
    'west_end': '1FC3H3bD-QGucif1646vNdLOeq8Lrf6qD',
    'downtown_older_buildings': '1MwBY-2tCzJmU1O_ngp4LqfzZfW4lZGbw',
    'the_leston': '1FdEhY-P4f7g0rAxCWYyJybXHDqHYSeqe',
    'rosenthal': '12rFEh5F8FbNqxzehpuPPI6sFbaVWe3FT',
    'edge': '1LZz2r1pmXrSV7wgclzAVu_jOcPp_hVkk',
    'eh': '1am88PUSHbGuow3Et0eTk0of_b1lp-QSM'
}

all_data = {}

for nickname, file_id in FILES_TO_SYNC.items():
    print(f"Downloading {nickname}...")
    request = service.files().get_media(fileId=file_id)
    file_stream = io.BytesIO()
    downloader = MediaIoBaseDownload(file_stream, request)
    
    done = False
    while done is False:
        status, done = downloader.next_chunk()
    
    # 3. Convert the downloaded Excel file into data
    file_stream.seek(0)
    df = pd.read_excel(file_stream)
    
    # 🚨 THE FIX: Replace all empty Excel cells (NaN) with empty text
    df = df.fillna("")
    
    # Store the data under its nickname
    all_data[nickname] = df.to_dict(orient='records')

# 4. Save everything into ONE big data.json file
with open('data.json', 'w') as f:
    json.dump(all_data, f)

print("Successfully updated all files and saved to data.json!")
