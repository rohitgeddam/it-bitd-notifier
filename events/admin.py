from django.contrib import admin
from .models import Event, EventFile, EventPhoto


class EventFileAdmin(admin.TabularInline):
    model = EventFile


class EventPhotoAdmin(admin.StackedInline):
    model = EventPhoto


class EventAdmin(admin.ModelAdmin):
    inlines = [EventFileAdmin, EventPhotoAdmin]
    model = Event


admin.site.register(Event, EventAdmin)
