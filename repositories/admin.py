from django.contrib import admin
from .models import AssetType, LogisticsAsset
from .models import DocumentRepository

@admin.register(AssetType)
class AssetTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(LogisticsAsset)
class LogisticsAssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'asset_type', 'state', 'status', 'updated_at')
    list_filter = ('state', 'asset_type', 'status')
    search_fields = ('name', 'location_description', 'contact_person')
    fieldsets = (
        ('Core Identification', {
            'fields': ('name', 'asset_type', 'state', 'status')
        }),
        ('Geospatial Location', {
            'fields': ('location_description', 'latitude', 'longitude')
        }),
        ('Operational Parameters', {
            'fields': ('capacity_details',)
        }),
        ('Emergency Management Contacts', {
            'fields': ('contact_person', 'contact_email', 'contact_phone')
        }),
    )




@admin.register(DocumentRepository)
class DocumentRepositoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'sub_type', 'state', 'published_year', 'uploaded_at')
    list_filter = ('category', 'state', 'sub_type', 'published_year')
    search_fields = ('title', 'description')
    ordering = ('-uploaded_at',)