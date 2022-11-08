

from django.http import JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def info(request, user_id):
    return JsonResponse(
        {
            'user_id': user_id,
            'online': 'Was 2 hours ago'
        }
    )


@require_GET
def username(request, user_id):
    return JsonResponse(
        {
            'user_id': user_id,
            'name': 'Ser',
            'surname': 'Melikyan',
        }
    )
