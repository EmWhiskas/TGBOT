import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and settings.py of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1O75BM0QxHI2l8n5rMewLm9LABKHeAUc1eKMeEtW7gEU"
# SAMPLE_RANGE_NAME = "Расписание замен 1 смены!C3:D11"
s = ''
mas = []
count = 0
def clear():
  global mas, count
  mas.clear()
  count = 0

def main(SAMPLE_RANGE_NAME):
  global mas, count, s
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
      count += 1
      try:
        try:
          answer = (f"{count} - {row[0]} {row[1]} ")
          mas.append(answer)
        except:
          answer = (f"{row[0]}")
          mas.append(answer)
      except:
        answer = ''
        mas.append(answer)

    if count == 8:
      mas.append('\n<i>Надо попахать⚰😵</i>')
      s = 'BAACAgIAAxkBAAMwZenFb808bdOP-8lC45nyjBbIrPkAAoVCAALBf0hLtWP5suE5mnc0BA'

    elif count == 7:
      mas.append('\n<i>Надо попахать⚰😵</i>')
      s = 'BAACAgIAAxkBAAOiZfhJD0aiDNIl_fri9cFFbgo8uhIAApFCAALBf0hLqTVLpz8AAfo9NAQ'

    elif count == 6:
      mas.append('\n<i>Можно потерпеть💃</i>')
      s = 'BAACAgIAAxkBAAMxZenFj1phzLFw2FjOT-Nq9NJMNL8AArRCAALBf0hLxLm38YLkTo40BA'
    elif count == 5:

      s = 'BAACAgIAAxkBAAMtZenEpDU8ZL-uBAAB6M1uRbczx8cfAAK0QgACwX9IS8S5t_GC5E6ONAQ'

    elif count == 4:
      mas.append('\n<i>Адихаем 🎰😋</i>')
      s='BAACAgIAAxkBAAIKxGXocWQURmh0DrfCYTzaAdlyXbA4AAJtQgACwX9IS_KqAXOW48nuNAQ'

    elif count == 3:
      mas.append('\n<i>Адихаем 🎰😋</i>')
      s = 'BAACAgIAAxkBAAMsZenERBdRT2n3YaKKeJH9qnYnHEgAAm1CAALBf0hL94GiT2YQFrU0BA'

    elif count ==2:
      mas.append('<i>Че реально</i>')
      s = 'BAACAgIAAxkBAAMqZenDToTpiETNhHndTfLPv2ABSBIAAtBCAALBf0hLzRn4gN5Fbf00BA'
    elif count == 1:
      s= 'BAACAgIAAxkBAAMrZenDtJqC1GcFY9wRaNNwiOLoMUEAAqFCAALBf0hLMk8YGYSi1dw0BA'
      mas.append('<i>Че реально</i>')
    print(mas)
    return mas



  except HttpError as err:
    print(err)
