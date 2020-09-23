from notion.client import NotionClient
import os.path
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2="add token here")

#-----------------------
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# link oauth service account key credentials down below
cred = os.path.join(BASE_DIR, 'Notion_linker/notion-sheet-link-fc29267e5941.json')
credentials = ServiceAccountCredentials.from_json_keyfile_name(cred, scope)

gc = gspread.authorize(credentials)
sh = gc.open("Responses")
print(sh)
worksheet = sh.get_worksheet(0)
cv = client.get_collection_view("database link here")




while True:
    cell_list = worksheet.findall("0")
    if len(cell_list) != 0:
        for i in cell_list:
            #logic for fetching data from spreadsheet
            name  = worksheet.cell(i.row, 2).value
            disc =  worksheet.cell(i.row, 3).value
            team  = worksheet.cell(i.row, 4).value
            print (name,team,disc)
            row = cv.collection.add_row()
            #name of row - notion db
            row.name = str(name)
            #field names in notion database below
            row.discord_name_and_tag = str(disc)
            row.team = str(team)
            worksheet.update_cell(i.row,i.col, '1')
    else:
        print ("sleeping for 6 mins")
        time.sleep(360)