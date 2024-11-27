from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
import logging
import os
import datetime

# Load environment variables
load_dotenv()
SENDER = os.getenv("SENDER")
FLIGHT_KEYWORD = os.getenv("FLIGHT_KEYWORD")
MEETING_KEYWORD = os.getenv("MEETING_KEYWORD")

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# File to store user credentials
TOKEN_FILE = "token.json"
CREDENTIALS_FILE = "credentials.json"

def authenticate_gmail():
    """Authenticate with Gmail API and return service object."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE)
    if not creds or not creds.valid:
        from google_auth_oauthlib.flow import InstalledAppFlow
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/gmail.readonly'])
        creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def authenticate_calendar():
    """Authenticate with Google Calendar API and return service object."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE)
    if not creds or not creds.valid:
        from google_auth_oauthlib.flow import InstalledAppFlow
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/calendar'])
        creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    return build('calendar', 'v3', credentials=creds)

def check_emails(service):
    """Check for emails matching criteria."""
    try:
        results = service.users().messages().list(userId='me', q=f'from:{SENDER}').execute()
        messages = results.get('messages', [])
        for msg in messages:
            message = service.users().messages().get(userId='me', id=msg['id']).execute()
            subject = next(header['value'] for header in message['payload']['headers'] if header['name'] == 'Subject')
            if FLIGHT_KEYWORD.lower() in subject.lower():
                send_flight_quotation()
            elif MEETING_KEYWORD.lower() in subject.lower():
                schedule_meeting()
    except HttpError as error:
        logging.error(f"Error fetching emails: {error}")

def send_flight_quotation():
    """Dummy function to send flight quotations."""
    logging.info("Sending flight quotation... (Replace this with actual email sending logic)")

def schedule_meeting():
    """Schedule a meeting using Google Calendar API."""
    try:
        service = authenticate_calendar()
        event = {
            'summary': 'Online Meeting',
            'start': {
                'dateTime': (datetime.datetime.utcnow() + datetime.timedelta(days=1)).isoformat() + 'Z',
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': (datetime.datetime.utcnow() + datetime.timedelta(days=1, hours=1)).isoformat() + 'Z',
                'timeZone': 'UTC',
            },
            'attendees': [
                {'email': SENDER},
            ],
        }
        event_result = service.events().insert(calendarId='primary', body=event).execute()
        logging.info(f"Meeting scheduled: {event_result.get('htmlLink')}")
    except HttpError as error:
        logging.error(f"Error scheduling meeting: {error}")

if __name__ == "__main__":
    try:
        logging.info("Authenticating with Gmail API...")
        gmail_service = authenticate_gmail()
        check_emails(gmail_service)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
