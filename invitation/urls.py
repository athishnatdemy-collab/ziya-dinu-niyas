from django.urls import path
from . import views

app_name = 'invitation'

urlpatterns = [
    path('', views.home, name='home'),
    path('dinu/', views.dinu, name='dinu'),
    path('dinu', views.dinu, name='dinu_bare'),
    path('ziya/', views.home, name='ziya'),
    path('ziya', views.home, name='ziya_bare'),
]


