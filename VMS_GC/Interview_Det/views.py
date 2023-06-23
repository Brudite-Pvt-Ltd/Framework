from django.shortcuts import render
from django.http import JsonResponse
from googleapiclient.discovery import build
from .google_calender import get_credentials
from .models import Interview
from datetime import timedelta
from google_auth_oauthlib.flow import Flow
from django.shortcuts import redirect
from django.http import HttpResponseBadRequest
from django.urls import reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pickle
from datetime import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar']


CREDENTIALS_FILE = 'credentials.pkl'


def save_credentials(credentials):
    with open(CREDENTIALS_FILE, 'wb') as f:
        pickle.dump(credentials, f)


def get_credentials():
    try:
        with open(CREDENTIALS_FILE, 'rb') as f:
            credentials = pickle.load(f)
            return credentials
    except FileNotFoundError:
        return None


@csrf_exempt
def create_event(credentials, interview):
    service = build('calendar', 'v3', credentials=credentials)

    interview_time = datetime.strptime(
        interview.interview_time, "%Y-%m-%dT%H:%M")

    event = {
        'summary': f"{interview.username}'s Interview",
        'description': f"Candidate Email: {interview.candidate_email}\n"
                       f"Interviewer Email: {interview.interviewer_email}\n"
                       f"Additional People Email: {interview.additional_people_email}\n"
                       f"Google Meet Link: {interview.google_meet_link}\n"
                       f"Remarks: {interview.remarks}",
        'start': {
            'dateTime': interview_time.isoformat(),
            'timeZone': 'Asia/Kolkata',  # Replace with your desired time zone
        },
        'end': {
            'dateTime': (interview_time + timedelta(hours=1)).isoformat(),
            'timeZone': 'Asia/Kolkata',  # Replace with your desired time zone
        },
        'attendees': [
            {'email': interview.candidate_email},
            {'email': interview.interviewer_email},
            {'email': interview.additional_people_email},
        ],
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    return event['id']


@csrf_exempt
def schedule_interview(request):
    stored_credentials = get_credentials()
    if stored_credentials is not None:
        credentials = stored_credentials
    elif 'code' in request.GET:
        # Authorization code is present in the query parameters
        authorization_code = request.GET['code']
        flow = Flow.from_client_secrets_file(
            'D:\Django\Framework\VMS_GC\Interview_Det\Credentials.json',
            scopes=['https://www.googleapis.com/auth/calendar'])
        flow.redirect_uri = 'http://127.0.0.1:8000/schedule-interview/'

        # Exchange the authorization code for credentials
        flow.fetch_token(
            authorization_response=request.build_absolute_uri(),
            code=authorization_code,
            access_type='offline',
            include_granted_scopes='true'
        )

        # Credentials obtained successfully
        # You can now use the credentials to make API requests
        credentials = flow.credentials

        # Save the credentials for future use
        save_credentials(credentials)
    else:
        # Authorization code is not present
        # Redirect the user to the authorization URL
        flow = Flow.from_client_secrets_file(
            'D:\Django\Framework\VMS_GC\Interview_Det\Credentials.json',
            scopes=['https://www.googleapis.com/auth/calendar'])
        flow.redirect_uri = 'http://127.0.0.1:8000/schedule-interview/'
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true')
        return redirect(authorization_url)

    if request.method == 'POST':
        # Extract data from the request
        username = request.POST.get('username')
        candidate_email = request.POST.get('candidate_email')
        interviewer_email = request.POST.get('interviewer_email')
        additional_people_email = request.POST.get(
            'additional_people_email')
        google_meet_link = request.POST.get('google_meet_link')
        interview_time = request.POST.get('interview_time')
        remarks = request.POST.get('remarks')

        # Create an instance of the Interview model
        interview = Interview(
            username=username,
            candidate_email=candidate_email,
            interviewer_email=interviewer_email,
            additional_people_email=additional_people_email,
            google_meet_link=google_meet_link,
            interview_time=interview_time,
            remarks=remarks
        )
        interview.save()

        # Create an event on the Google Calendar using the obtained credentials
        event_id = create_event(credentials, interview)
        print("this is your event id", event_id)
        return HttpResponse(event_id, "Successfully scheduled the interview.")
    else:
        return render(request, 'schedule_interview.html')


def update_interview_time(credentials, interview_id, new_interview_time):
    service = build('calendar', 'v3', credentials=credentials)

    interview = Interview.objects.get(id=interview_id)
    old_interview_time = interview.interview_time

    event = service.events().get(calendarId='primary',
                                 eventId=interview.event_id).execute()

    event['start']['dateTime'] = new_interview_time.isoformat()
    event['end']['dateTime'] = (
        new_interview_time + timedelta(hours=1)).isoformat()

    updated_event = service.events().update(
        calendarId='primary', eventId=interview.event_id, body=event).execute()

    interview.interview_time = new_interview_time
    interview.save()

    return updated_event['id']
