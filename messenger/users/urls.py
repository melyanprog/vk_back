from django.urls import path

from .views import username, info

urlpatterns = [
    path('username/<int:user_id>', username, name='user full name info'),
    path('meta/<int:user_id>', info, name='user info')
]
