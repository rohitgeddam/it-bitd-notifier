import django_filters
from .models import Job

from .models import OFFER_TYPE, APPLICATION_TYPE


class JobFilter(django_filters.FilterSet):

    offer_type = django_filters.ChoiceFilter(
        label="Offer Type", choices=OFFER_TYPE, method="filter_by_offer_type"
    )
    application_type = django_filters.ChoiceFilter(
        label="Campus Type", choices=APPLICATION_TYPE, method="filter_by_campus_type"
    )

    class Meta:
        model = Job
        fields = {
            "title": [
                "icontains",
            ]
        }

    def filter_by_offer_type(self, queryset, name, value):
        expression = OFFER_TYPE[0][0] if value == "I" else OFFER_TYPE[1][0]
        return queryset.filter(offer_type=expression)

    def filter_by_campus_type(self, queryset, name, value):
        expression = APPLICATION_TYPE[0][0] if value == "OF" else OFFER_TYPE[1][0]
        return queryset.filter(application_type=expression)
