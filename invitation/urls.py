from django.urls import path
from . import views

app_name = 'invitation'

urlpatterns = [
    path('', views.home, name='home'),
    path('dinu/', views.dinu, name='dinu'),
    path('dinu', views.dinu, name='dinu_bare'),
    path('ziya/', views.home, name='ziya'),
    path('ziya', views.home, name='ziya_bare'),
    path('receptoin-4-7/', views.reception, name='receptoin_4_7'),
    path('receptoin-4-7', views.reception, name='receptoin_4_7_bare'),
    path('reception-4-7/', views.reception, name='reception_4_7'),
    path('reception-4-7', views.reception, name='reception_4_7_bare'),
    path('reception/', views.reception, name='reception'),
    path('reception', views.reception, name='reception_bare'),
    path('receptoin/', views.reception, name='receptoin'),
    path('receptoin', views.reception, name='receptoin_bare'),
]


