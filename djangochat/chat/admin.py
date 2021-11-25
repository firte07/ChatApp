from django.contrib import admin
from .models import Room, Message, Invitation

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Invitation)
