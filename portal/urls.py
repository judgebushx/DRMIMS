# portal/urls.py
from django.urls import path
from .views import FAQListView, home, BlogNewsListView, BlogNewsDetailView, dashboards_view

app_name = 'portal'

urlpatterns = [
    path('', home, name='home'),
    path('faq/', FAQListView.as_view(), name='faq_list'), 
    path('news/', BlogNewsListView.as_view(), name='news_list'),
    path('news/<slug:slug>/', BlogNewsDetailView.as_view(), name='news_detail'),
    path('dashboards/', dashboards_view, name='dashboards'),
]