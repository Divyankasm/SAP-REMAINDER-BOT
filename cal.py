from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/calendar']
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build('calendar', 'v3', credentials=creds)

calendar_list = service.calendarList().list().execute()

for cal in calendar_list['items']:
    print(f"📅 {cal['summary']} - ID: {cal['id']}")
