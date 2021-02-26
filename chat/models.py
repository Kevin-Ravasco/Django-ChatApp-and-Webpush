from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(default="/static/media/images/default/default.png")
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SingleChat(models.Model):
    participant1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='participant1')
    participant2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='participant2')

    def __str__(self):
        return "Chat by {} and {}.".format(self.participant1.name, self.participant2.name)


def get_users_chat(user, participant):
    # try to get the chat in reverse orders, create one if it does not exist
    try:
        chat = SingleChat.objects.get(participant1=user, participant2=participant)
    except ObjectDoesNotExist:
        try:
            chat = SingleChat.objects.get(participant1=participant, participant2=user)
        except ObjectDoesNotExist:
            chat = SingleChat.objects.create(participant1=user, participant2=participant)
    return chat


class Messages(models.Model):
    chat = models.ForeignKey(SingleChat, on_delete=models.CASCADE)
    by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



