from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>", views.JobDetailView.as_view(), name="job_detail"),
    path("", views.JobList.as_view(), name="job_list"),
]
