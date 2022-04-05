import json
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

print(os.environ['PROJECT_ID'])

# client_secret.jsonを作成
client_secret_dict = {
  "type": "service_account",
  "project_id": os.environ['PROJECT_ID'],
  "private_key_id": os.environ['PRIVATE_KEY_ID'],
  "private_key": os.environ['PRIVATE_KEY'],
  "client_email": os.environ['CLIENT_EMAIL'],
  "client_id": os.environ['CLIENT_ID'],
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": os.environ['CLIENT_X599_CERT_URL'],
}
with open('client_secret.json', 'w') as f:
    json.dump(client_secret_dict, f, indent=2, ensure_ascii=False)

# use creds to create a client to interact with the Google Drive API
scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("晴楽の英単語帳").sheet1
