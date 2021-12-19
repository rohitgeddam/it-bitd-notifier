from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Event, EventFile, EventPhoto
from .filters import EventFilter
from datetime import datetime

# Create your views here.
class EventList(ListView):
    """List All Notices"""

    model = Event
    context_object_name = "events"
    template_name = "events/list.html"
    # ordering = [
    #     "-updated_on",
    # ]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = EventFilter(self.request.GET, queryset=self.get_queryset())
        return context


class EventDetailView(DetailView):

    model = Event
    template_name = "events/detail.html"
    order_by = "-date"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["files"] = EventFile.objects.filter(event=self.object)
        context["photos"] = EventPhoto.objects.filter(event=self.object)

        return context
