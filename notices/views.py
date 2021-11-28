from django.shortcuts import render
from django.views.generic import ListView

from .models import Notice

# Create your views here.
class NoticeList(ListView):
    """List All Notices"""

    model = Notice
    context_object_name = "notices"
    template_name = "notices/list.html"
