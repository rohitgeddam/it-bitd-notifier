from django.contrib import admin
from .models import Notice, NoticeFile


class NoticeInLine(admin.TabularInline):
    model = NoticeFile


class NoticeAdmin(admin.ModelAdmin):
    inlines = [
        NoticeInLine,
    ]


admin.site.register(Notice, NoticeAdmin)
