import os
import datetime

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_calendar_service():
    """Authenticate and return a Google Calendar API service."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    return service


def create_event(service, calendar_id: str, title: str, due_date: datetime.datetime, reminders=None):
    """
    Create a full-day event on due_date with popup reminders.

    reminders: list of minutes before the event (e.g., [10080, 4320, 1440])
    """
    if reminders is None:
        reminders = [7 * 24 * 60, 3 * 24 * 60, 24 * 60]

    start_date = due_date.date().isoformat()
    end_date = (due_date.date() + datetime.timedelta(days=1)).isoformat()

    event = {
        'summary': title,
        'start': {'date': start_date},
        'end': {'date': end_date},
        'reminders': {
            'useDefault': False,
            'overrides': [{'method': 'popup', 'minutes': m} for m in reminders],
        },
    }
    return service.events().insert(calendarId=calendar_id, body=event).execute()


def list_upcoming_events(service, calendar_id: str, max_results=10):
    """
    Return upcoming events from now.
    """
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = (
        service.events()
        .list(
            calendarId=calendar_id,
            timeMin=now,
            maxResults=max_results,
            singleEvents=True,
            orderBy='startTime',
        )
        .execute()
    )
    return events_result.get('items', [])