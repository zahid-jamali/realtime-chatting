from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.CustomUser)
admin.site.register(models.chat_rooms)
admin.site.register(models.chattings)