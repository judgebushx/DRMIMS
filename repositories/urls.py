from django.urls import path
from .views import LogisticsAssetListView, DocumentHubListView

app_name = 'repositories'

urlpatterns = [
    path('logistics/', LogisticsAssetListView.as_view(), name='logistics_list'),
    
    # DM Plans Page Mapping
    path('plans/', DocumentHubListView.as_view(
        category_filter='DM_PLAN', 
        page_title='Disaster Management Plans Repository'
    ), name='plans_repository'),
    
    # Risk Profiles Page Mapping
    path('risk-profiles/', DocumentHubListView.as_view(
        category_filter='RISK_PROFILE', 
        page_title='Risk Profile Repository'
    ), name='risk_repository'),
    
    # Area Profiles Page Mapping
    path('area-profiles/', DocumentHubListView.as_view(
        category_filter='AREA_PROFILE', 
        page_title='Area Profile Repository'
    ), name='area_repository'),
]