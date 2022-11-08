from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from time import time


@require_GET
def homepage(request):
    return render(request, 'index.html')


@csrf_exempt
@require_POST
def create_chat(request):
    chats = [
        {
            'chat_id': 1,
            'username': 'Ser',
            'message': 'Hello'
        }, {
            'chat_id': 2,
            'username': request.POST.get('name'),
            'message': request.POST.get('message')
        }
    ]

    return JsonResponse(chats, safe=False)


@require_GET
def chat_list(request):
    chat_dialog = {
        'chats': [
            {
                'chat_id': 1,
                'username': 'Ed Melikyan',
                'message': 'Hi!'
            },
            {
                'chat_id': 2,
                'username': 'Ser Melikyan',
                'message': ['Hello!'][-1]
            },

        ]
    }

    return JsonResponse(chat_dialog)
