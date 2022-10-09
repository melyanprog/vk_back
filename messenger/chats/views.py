from django.http import JsonResponse
from django.shortcuts import render


def chat_list(request):
    return JsonResponse({'chats': []})
