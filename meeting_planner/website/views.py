from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from meetings.models import Meeting


def welcome(request):
    return render(request, 'website/welcome.html', {
        'message': 'This is the message.',
        'num_meetings': Meeting.objects.count()
    })


def date(request):
    return HttpResponse('This page is saved at: ' + str(datetime.now()))


def about(request):
    return HttpResponse('This is the about me page.')