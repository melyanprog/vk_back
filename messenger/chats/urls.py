from django.urls import path
from chats.views import chat_list

urlpatterns = [
    path('', chat_list, name='chat_list'),
    #path('category/<int:pk>/', 'chat_category', name='chat_category'),
    #path('<chat_id>/', 'chat_setail', name='chat_detail'),
]
