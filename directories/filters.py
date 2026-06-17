import django_filters
from django.db import models
from .models import EmergencyContact

class EmergencyContactFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method='filter_by_all_text',
        label="Search Agency, Name, Title, or Frequencies",
        widget=django_filters.widgets.CSVWidget(attrs={'class': 'form-control', 'placeholder': 'Search contacts (e.g. Fire, DECEM, Smith)...'})
    )

    class Meta:
        model = EmergencyContact
        fields = ['state', 'sector', 'is_24_7_operational']

    def filter_by_all_text(self, queryset, name, value):
        return queryset.filter(
            models.Q(agency_name__icontains=value) |
            models.Q(focal_person__icontains=value) |
            models.Q(job_title__icontains=value) |
            models.Q(notes__icontains=value)
        )