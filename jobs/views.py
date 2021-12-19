from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Job
from .filters import JobFilter

# Create your views here.
class JobList(ListView):
    """List All Notices"""

    model = Job
    context_object_name = "jobs"
    template_name = "jobs/list.html"
    ordering = [
        "-updated_on",
    ]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = JobFilter(self.request.GET, queryset=self.get_queryset())
        return context


class JobDetailView(DetailView):

    model = Job
    template_name = "jobs/detail.html"
    # order_by = "-posted_on"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["files"] = EventFile.objects.filter(event=self.object)
        # context["photos"] = EventPhoto.objects.filter(event=self.object)

        return context
