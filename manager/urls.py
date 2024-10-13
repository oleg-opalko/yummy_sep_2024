from django.urls import path

from manager.views import users_reservation

app_name = 'manager'
urlpatterns = [
    path('users_reservation/', users_reservation, name='users_reservation'),
]