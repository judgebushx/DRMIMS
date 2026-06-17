import json
from django.shortcuts import render
from django.views.generic import ListView
from .models import LogisticsAsset
from .filters import LogisticsAssetFilter
from .models import DocumentRepository
from .filters import DocumentFilter


class LogisticsAssetListView(ListView):
    model = LogisticsAsset
    template_name = 'repositories/logistics_list.html'
    context_object_name = 'assets'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Apply the Django-Filter to our baseline queryset
        self.filterset = LogisticsAssetFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterform'] = self.filterset.form
        
        # Serialize only our currently filtered coordinates into a lightweight JSON array for Leaflet.js
        map_points = []
        for asset in self.get_queryset():
            if asset.latitude and asset.longitude:
                map_points.append({
                    'name': asset.name,
                    'type': asset.asset_type.name,
                    'state': asset.get_state_display(),
                    'status': asset.get_status_display(),
                    'lat': float(asset.latitude),
                    'lng': float(asset.longitude),
                    'capacity': asset.capacity_details[:100] + '...' if len(asset.capacity_details) > 100 else asset.capacity_details
                })
        
        context['map_points_json'] = json.dumps(map_points)
        return context
    



class DocumentHubListView(ListView):
    model = DocumentRepository
    template_name = 'repositories/document_vault.html'
    context_object_name = 'documents'
    paginate_by = 15
    
    # Setting default property configuration layers
    category_filter = None 
    page_title = "Document Repository"

    def get_queryset(self):
        # 1. Filter dataset down to the explicit category designated by the URL route
        queryset = super().get_queryset().filter(category=self.category_filter)
        # 2. Attach the Django-Filter layer for granular query evaluations
        self.filterset = DocumentFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterform'] = self.filterset.form
        context['page_title'] = self.page_title
        context['current_category'] = self.category_filter
        return context