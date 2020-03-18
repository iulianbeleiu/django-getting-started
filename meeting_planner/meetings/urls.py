from django.urls import path
from . import views
from meetings.views import detail, rooms

urlpatterns = [
    path('<int:id>', detail, name='detail'),
    path('rooms', rooms, name='rooms'),
]