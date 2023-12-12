from django.contrib import admin
from django.urls import path

import chatbot.views

urlpatterns = [
    path('', chatbot.views.chat, name = 'chatter'),
]