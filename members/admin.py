from django.contrib import admin

# Register your models here.
from .models import Members
from .models import Task

admin.site.register(Members)
admin.site.register(Task)