from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting, Room

# MVT (Model View Template)

# Request => http://127.0.0.1:8000/welcome.html
# v.1
# def welcome(request):
#     return HttpResponse('Welcome to the Meeting Planner App')


def welcome(request):
    data = Meeting.objects.all() # SQL => select * from Meetings
    return render(
        request,
        'website/welcome.html',
        {'message': 'This data was sent from the views to the template',
         'num_meetings': Meeting.objects.count(),
         'meetings': data
         }
    )


# Request => http://127.0.0.1:8000/date
def date(request):
    return HttpResponse(f'This page serverd {datetime.now()}')
