from django.contrib import admin
from .models import Computer, Command, Output

admin.site.register(Computer)
admin.site.register(Command)
admin.site.register(Output)