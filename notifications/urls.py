from django.urls import path
from notifications.views import messages
app_name='notifications'
urlpatterns=[
path('messages',messages,name='messages'),
]