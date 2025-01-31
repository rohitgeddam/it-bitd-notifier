"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

admin.site.site_header = "NOTIFIER IT BITD ADMIN"
admin.site.site_title = "NOTIFIER IT BITD ADMIN PORTAL"
admin.site.index_title = "Welcome to Notifier I.T BIT-D admin portal"

urlpatterns = [
    path("api/v1/", include("apis.v1.urls"), name="api-v1"),
    path("admin/", admin.site.urls),
    path("notices/", include("notices.urls"), name="notices"),
    path("events/", include("events.urls")),
    path("jobs/", include("jobs.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("users/", include("users.urls")),
    path("", views.HomePageView.as_view(), name="home"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
