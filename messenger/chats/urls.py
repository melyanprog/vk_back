from django.urls import path

from .views import chat_list, chat_list, create_chat

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('<int:chat_id>/', chat_list, name='chat_page'),
    path('create/', create_chat, name='create_chat'),
]
