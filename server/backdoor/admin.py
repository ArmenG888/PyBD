from django.contrib import admin
from .models import Computer, Command, Output, Image

admin.site.register(Computer)
admin.site.register(Command)
admin.site.register(Image)
admin.site.register(Output)