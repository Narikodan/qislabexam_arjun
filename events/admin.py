from django.contrib import admin

from .models import CustomUser, Event, House

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Event)
admin.site.register(House)
