from django.contrib import admin
from convertPixelArt.models import Threads


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('threadID', 'threadName', 'red', 'green', 'blue', 'threadHex')
    ordering = ['threadID']

admin.site.register(Threads, ThreadAdmin)