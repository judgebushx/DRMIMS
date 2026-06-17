import django_filters
from .models import LogisticsAsset
from .models import DocumentRepository
from django.db import models


class LogisticsAssetFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains', 
        label="Search Asset Name",
        widget=django_filters.widgets.CSVWidget(attrs={'class': 'form-control', 'placeholder': 'e.g. Airport, Warehouse...'})
    )
    
    class Meta:
        model = LogisticsAsset
        fields = ['state', 'asset_type', 'status']



class DocumentFilter(django_filters.FilterSet):
    # Free-text keyword indexers matching titles or descriptions
    search = django_filters.CharFilter(
        method='filter_by_keyword',
        label="Search Title & Content Keywords",
        widget=django_filters.widgets.CSVWidget(attrs={'class': 'form-control', 'placeholder': 'Type keywords (e.g., Typhoon, Pohnpei, SOP)...'})
    )

    class Meta:
        model = DocumentRepository
        fields = ['state', 'sub_type', 'published_year']

    def filter_by_keyword(self, queryset, name, value):
        return queryset.filter(
            models.Q(title__icontains=value) | models.Q(description__icontains=value)
        )