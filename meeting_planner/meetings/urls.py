from django.urls import path
from . import views
from meetings.views import detail, rooms

urlpatterns = [
    path('<int:id>', detail, name='detail'),
    path('rooms', rooms, name='rooms'),
    path('new', views.new, name='new'),
    path('new_form', views.new_form, name='new_form')
]