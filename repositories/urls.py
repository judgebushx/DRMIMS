from django.urls import path
from .views import LogisticsAssetListView, DocumentHubListView

app_name = 'repositories'

urlpatterns = [
    path(
        'logistics/',
        LogisticsAssetListView.as_view(),
        name='logistics_list'
    ),

    # Disaster Management Plans
    path(
        'plans/',
        DocumentHubListView.as_view(
            category_filter='DM_PLAN',
            page_title='Documents Repository'
        ),
        name='plans_repository'
    ),

    # Risk Profiles
    path(
        'risk-profiles/',
        DocumentHubListView.as_view(
            category_filter='RISK_PROFILE',
            page_title='Risk Profile Repository'
        ),
        name='risk_repository'
    ),

    # Area Profiles
    path(
        'area-profiles/',
        DocumentHubListView.as_view(
            category_filter='AREA_PROFILE',
            page_title='Area Profile Repository'
        ),
        name='area_repository'
    ),

    # Assessment Tools
    path(
        'assessment-tools/',
        DocumentHubListView.as_view(
            category_filter='ASSESSMENT TOOLS',
            page_title='Assessment Tools Repository'
        ),
        name='assessment_tools_repository'
    ),
]