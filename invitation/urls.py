from django.urls import path
from . import views

app_name = 'invitation'

urlpatterns = [
    path('', views.home, name='home'),
    path('dinu/', views.dinu, name='dinu'),
    path('dinu', views.dinu, name='dinu_bare'),
    path('ziya/', views.home, name='ziya'),
    path('ziya', views.home, name='ziya_bare'),
    # Reception 4:00 PM – 7:00 PM
    path('receptoin-4-7/', views.reception, name='receptoin_4_7'),
    path('receptoin-4-7', views.reception, name='receptoin_4_7_bare'),
    path('reception-4-7/', views.reception, name='reception_4_7'),
    path('reception-4-7', views.reception, name='reception_4_7_bare'),
    path('reception/', views.reception, name='reception'),
    path('reception', views.reception, name='reception_bare'),
    path('receptoin/', views.reception, name='receptoin'),
    path('receptoin', views.reception, name='receptoin_bare'),
    # Reception 7:00 PM – 10:00 PM
    path('reception-7-10/', views.reception_7_10, name='reception_7_10'),
    path('reception-7-10', views.reception_7_10, name='reception_7_10_bare'),
    path('receptoin-7-10/', views.reception_7_10, name='receptoin_7_10'),
    path('receptoin-7-10', views.reception_7_10, name='receptoin_7_10_bare'),
    path('reception_7_10/', views.reception_7_10, name='reception_7_10_underscore'),
    path('reception_7_10', views.reception_7_10, name='reception_7_10_underscore_bare'),
]
