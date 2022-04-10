from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json

# 사용자 인증
scope = {
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
}

json_key_path = "./key.json"
json_sheetdata_path = "./sheetdata.json"
json_file = open(json_sheetdata_path, 'r', encoding='utf-8')
json_data = json.load(json_file)

# json load sheet key load
print("json_data['sheet_key']: ", json_data['sheet_key'])
json_sheet_key = json_data['sheet_key']

credential = ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scope)
gc = gspread.authorize(credential)