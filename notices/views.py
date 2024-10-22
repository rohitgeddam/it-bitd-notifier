from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Notice, NoticeFile
from .filters import NoticeFilter


# Create your views here.
class NoticeList(ListView):
    """List All Notices"""

    model = Notice
    context_object_name = "notices"
    template_name = "notices/list.html"
    ordering = [
        "-updated_on",
    ]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = NoticeFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NoticeDetailView(DetailView):

    model = Notice
    template_name = "notices/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["files"] = NoticeFile.objects.filter(notice=self.object)
        return context
