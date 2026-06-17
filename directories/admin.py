from django.contrib import admin
from .models import ContactSector, EmergencyContact

@admin.register(ContactSector)
class ContactSectorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ('agency_name', 'focal_person', 'state', 'sector', 'is_24_7_operational')
    list_filter = ('state', 'sector', 'is_24_7_operational')
    search_fields = ('agency_name', 'focal_person', 'notes')