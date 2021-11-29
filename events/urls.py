from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>", views.EventDetailView.as_view(), name="event_detail"),
    path("", views.EventList.as_view(), name="event_list"),
]
