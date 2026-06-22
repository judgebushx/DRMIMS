import django_filters
from django import forms
from django.db.models import Q
from .models import EmergencyContact

class EmergencyContactFilter(django_filters.FilterSet):
    # 1. We explicitly define 'search' to catch the text field submission
    # 2. We inject Bootstrap's 'form-control' directly into the widget attributes so {{ filterform.search }} renders perfectly styled
    search = django_filters.CharFilter(
        method='filter_by_free_text',
        label='Free Text Indexing',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search agency, person, or notes...'
        })
    )

    class Meta:
        model = EmergencyContact
        # These match the manually coded HTML 'name' attributes in your search card dropdowns/checkboxes
        fields = ['state', 'sector', 'is_24_7_operational']

    def filter_by_free_text(self, queryset, name, value):
        """Evaluates a single search string across multiple text horizons."""
        if value:
            return queryset.filter(
                Q(agency_name__icontains=value) |
                Q(focal_person__icontains=value) |
                Q(job_title__icontains=value) |
                Q(notes__icontains=value)
            )
        return queryset