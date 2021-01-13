from django.contrib import admin
from .models import Angulo

class AnguloAdmin(admin.ModelAdmin):
    list_display = ("id", "hour", "minute", "angle", "date",)

admin.site.register(Angulo, AnguloAdmin)