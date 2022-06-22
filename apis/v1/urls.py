from django.urls import include, path
from rest_framework.authtoken import views
from .views import NoticeListView, JobListView, EventsListView, Profile, PushNotificationView

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('notices/list/', NoticeListView.as_view(), name="notices_list"),
    path('jobs/list/', JobListView.as_view(), name="jobs_list"),
    path('events/list/', EventsListView.as_view(), name="events_list"),
    path('me/', Profile.as_view(), name="user"),
    path('push_token/', PushNotificationView.as_view(), name="push_tokens")
]   