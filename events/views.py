from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Event

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


class EventDetailView(DetailView):

    model = Event
    template_name = "events/detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
