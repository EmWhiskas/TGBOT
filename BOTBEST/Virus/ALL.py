import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import settings as s
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and settings.py of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1O75BM0QxHI2l8n5rMewLm9LABKHeAUc1eKMeEtW7gEU"
# SAMPLE_RANGE_NAME = "Смена1!C3:D48"
num_rows = 0
mas = []
count = 0
count2 = 1
def clear():
  global mas, count
  mas.clear()
  count = 0

def main(SAMPLE_RANGE_NAME):
  global mas, count, count2
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("pas/token.json"):
    creds = Credentials.from_authorized_user_file("pas/token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "pas/credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("pas/token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      mas.append('Информация не найдена')
      return mas

    for row in values:
        count2 += 1
        if count2 == s.Понедельник1:
            mas.append('<b>ПОНЕДЕЛЬНИК😖🇷🇺</b>')
        elif count2 == s.Вторник1:
            mas.append('<b>ВТОРНИК😣</b>')
        elif count2 == s.Среда1:
            mas.append('<b>СРЕДА😏</b>')
        elif count2 == s.Четверг1:
            mas.append('<b>ЧЕТВЕРГ😜</b>')
        elif count2 == s.Пятница1:
            mas.append('<b>ПЯТНИЦА🥳</b>')



        try:

            try:
                count += 1
                answer = (f"{count} - {row[0]} {row[1]} ")
                mas.append(answer)
            except:
                answer = (f"{count} - <b>{row[0]}</b>")
                mas.append(answer)
        except:
            count = 0
            answer = ''
            mas.append(answer)



    print(mas)
    return mas




  except HttpError as err:
    print(err)
