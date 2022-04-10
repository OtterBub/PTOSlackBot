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
# print("json_data['sheet_key']: ", json_data['sheet_key'])
json_sheet_key = json_data['sheet_key']

credential = ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scope)
gc = gspread.authorize(credential)

# Function
def test_spreadsheet(doc:gspread.Spreadsheet):
    sheet:gspread.Worksheet = doc.worksheet("Sheet1")
    test_val = sheet.get('A1')
    print(test_val)

    return sheet

# Use URL
spreadsheet_url = "https://docs.google.com/spreadsheets/d/" + json_sheet_key + "/edit?usp=sharing"
doc_url = gc.open_by_url(spreadsheet_url)

print("doc_url")
test_spreadsheet(doc_url)

# OR

# Use Key
spreadsheet_key = json_sheet_key
doc_key = gc.open_by_key(spreadsheet_key)

print("doc_key")
test_spreadsheet(doc_key)

# OR

# Use Name
spreadsheet_name = "Slack Bot Test Sheet"
doc_name = gc.open(spreadsheet_name)

print("doc_name")
sheet = test_spreadsheet(doc_name)
sheet.update('A1', "Test Update Value")