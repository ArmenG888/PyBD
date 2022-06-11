from django.contrib import admin
from .models import Computer, Command

admin.site.register(Computer)
admin.site.register(Command)