from django.urls import path
from .views import DirectoryListView

app_name = 'directories'

urlpatterns = [
    path('', DirectoryListView.as_view(), name='directory_list'),
]