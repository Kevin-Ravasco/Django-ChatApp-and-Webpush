from django.contrib import admin

from .models import Profile, SingleChat, Messages

admin.site.register(Profile)
admin.site.register(SingleChat)
admin.site.register(Messages)
