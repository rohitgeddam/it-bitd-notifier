from django.views.generic.base import TemplateView
from events.models import Event
from notices.models import Notice
from jobs.models import Job


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["notices"] = Notice.objects.all()[:5]
        context["events"] = Event.objects.all()[:5]
        context["jobs"] = Job.objects.all()[:5]
        return context
