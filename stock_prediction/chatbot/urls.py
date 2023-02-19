from django.urls import path
from . import chatbot

urlpatterns = [
    path('chatbot/', chatbot.chatbot_response, name='chatbot_response'),
]