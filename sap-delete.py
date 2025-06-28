from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

# Load credentials
SERVICE_ACCOUNT_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/calendar']
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build('calendar', 'v3', credentials=creds)

# Define your time window (wide enough to catch all events)
time_min = '2025-06-24T00:00:00+05:30'
time_max = '2025-07-31T23:59:59+05:30'

# Fetch all events in the time range
events_result = service.events().list(
    calendarId='primary',
    timeMin=time_min,
    timeMax=time_max,
    singleEvents=True,
    orderBy='startTime'
).execute()

events = events_result.get('items', [])

count = 0
for event in events:
    if 'SAP ABAP Training' in event.get('summary', ''):
        event_id = event['id']
        service.events().delete(calendarId='primary', eventId=event_id).execute()
        print(f"🗑️ Deleted: {event['summary']} on {event['start']['dateTime']}")
        count += 1

if count == 0:
    print("✅ No SAP ABAP events found to delete.")
else:
    print(f"✅ Deleted {count} SAP ABAP training events.")
