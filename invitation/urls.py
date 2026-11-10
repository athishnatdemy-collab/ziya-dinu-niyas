from django.urls import path
from . import views

app_name = 'invitation'

urlpatterns = [
    path('', views.home, name='home'),
]
