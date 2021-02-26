from django.urls import path

from .views import home, room, get_chat_messages, get_participant_info


urlpatterns = [
    path('', home, name='home'),
    path('messages/<int:id>/', get_chat_messages, name='get_chat_messages'),
    path('participant/<int:id>/', get_participant_info, name='get_participant_info'),
    # path('<str:room_name>/', room, name='room'),
]

