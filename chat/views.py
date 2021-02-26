from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from .models import Profile, SingleChat, Messages, get_users_chat


def home(request):
    user = request.user
    profiles = Profile.objects.exclude(user=user)
    webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')

    context = {'profiles': profiles, 'user': user, 'vapid_key': vapid_key}
    return render(request, 'index.html', context)


def get_chat_messages(request, id):
    participant = Profile.objects.get(id=id)
    chat = get_users_chat(user=request.user.profile, participant=participant)
    messages = Messages.objects.filter(chat=chat).order_by('timestamp')
    context = {'messages': messages}
    return render(request, 'chats.html', context)


# def get_chat_messages(request, id):
#     participant = Profile.objects.get(id=id)
#     # try to get the chat in reverse orders, create one if it does not exist
#     try:
#         chat = SingleChat.objects.get(participant1=request.user.profile, participant2=participant)
#     except ObjectDoesNotExist:
#         try:
#             chat = SingleChat.objects.get(participant1=participant, participant2=request.user.profile)
#         except ObjectDoesNotExist:
#             chat = SingleChat.objects.create(participant1=request.user.profile, participant2=participant)
#     messages = Messages.objects.filter(chat=chat).order_by('timestamp').values()
#     data = list(messages)
#     return JsonResponse(data, safe=False)


def get_participant_info(request, id):
    participant = Profile.objects.get(id=id)
    context = {'participant': participant}
    return render(request, 'header.html', context)


def room(request, room_name):
    context = {'room_name': room_name}
    return render(request, 'chat/room.html', context)


# @require_POST
# def send_push(request):
#     try:
#         body = request.body
#         data = json.loads(body)
#
#         if 'head' not in data or 'body' not in data or 'id' not in data:
#             return JsonResponse(status=400, data={"message": "Invalid data format"})
#
#         user_id = data['id']
#         user = get_object_or_404(User, pk=user_id)
#         payload = {'head': data['head'], 'body': data['body'], 'icon': 'https://i.imgur.com/dRDxiCQ.png', 'url': 'https://www.youtube.com'}
#         send_user_notification(user=user, payload=payload, ttl=1000)
#
#         return JsonResponse(status=200, data={"message": "Web push successful"})
#     except TypeError:
#         return JsonResponse(status=500, data={"message": "An error occurred"})