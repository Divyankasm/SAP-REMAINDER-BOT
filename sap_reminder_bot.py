from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load credentials
SERVICE_ACCOUNT_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/calendar']
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build('calendar', 'v3', credentials=creds)

# SAP Training Schedule
training_schedule = [
    {"date": "2025-06-25", "time": "09:30", "title": "SAP ABAP Training"},
    {"date": "2025-06-26", "time": "09:30", "title": "SAP ABAP Training"},
    {"date": "2025-07-03", "time": "09:30", "title": "SAP ABAP Training"},
    {"date": "2025-07-09", "time": "09:30", "title": "SAP ABAP Training"},
    {"date": "2025-07-12", "time": "09:30", "title": "SAP ABAP Training"},
    {"date": "2025-07-16", "time": "09:30", "title": "SAP ABAP Training"},
    {"date": "2025-07-19", "time": "09:30", "title": "SAP ABAP Training"},
    {"date": "2025-07-23", "time": "09:30", "title": "SAP ABAP Training"},
    {"date": "2025-07-26", "time": "09:30", "title": "SAP ABAP Training"},
    {"date": "2025-07-30", "time": "09:30", "title": "SAP ABAP Training"},
]

# Add events
for event in training_schedule:
    start_time = f"{event['date']}T{event['time']}:00+05:30"
    end_time = f"{event['date']}T13:30:00+05:30"  # 4-hour session

    event_body = {
        'summary': event['title'],
        'start': {
            'dateTime': start_time,
            'timeZone': 'Asia/Kolkata'
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Asia/Kolkata'
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 10}
            ]
        }
    }

    created_event = service.events().insert(calendarId='divyank00009856@gmail.com', body=event_body).execute()
    print(f"✅ Event created: {created_event.get('summary')} on {event['date']}")
