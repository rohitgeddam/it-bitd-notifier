import django_filters
from .models import Notice


class NoticeFilter(django_filters.FilterSet):
    class Meta:
        model = Notice
        fields = {
            "title": [
                "icontains",
            ]
        }
