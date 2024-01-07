from django.contrib import admin
from .models import Meeting, Room
# Register your models here.

# Aşağıdaki kod bloğu vasıtasıyla artık admin ilgili model üzerinden CRUD işlemi yapabilecek
admin.site.register(Meeting)
admin.site.register(Room)
