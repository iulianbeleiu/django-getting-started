from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

def welcome(request):
    return HttpResponse('Welcome to the meeting planner.')

def date(request):
    return HttpResponse('This page is saved at: ' + str(datetime.now()))

def about(request):
    return HttpResponse('This is the about me page.')