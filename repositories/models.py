from django.db import models

class AssetType(models.Model):
    """Classifies the type of logistical asset (e.g., Warehouse, Sea Port, Airport, Storage Facility)"""
    name = models.CharField(max_length=100, unique=True)
    icon_marker = models.CharField(max_length=50, default='marker', help_text="Map marker styling key")

    def __str__(self):
        return self.name

class LogisticsAsset(models.Model):
    """Tracks critical disaster response infrastructure across FSM States"""
    STATE_CHOICES = [
        ('NATIONAL', 'National Government'),
        ('CHUUK', 'Chuuk State'),
        ('KOSRAE', 'Kosrae State'),
        ('POHNPEI', 'Pohnpei State'),
        ('YAP', 'Yap State'),
    ]

    STATUS_CHOICES = [
        ('OPERATIONAL', 'Fully Operational'),
        ('DAMAGED', 'Damaged / Limited Capacity'),
        ('INACTIVE', 'Inactive / Closed'),
    ]

    name = models.CharField(max_length=255)
    asset_type = models.ForeignKey(AssetType, on_delete=models.PROTECT, related_name='assets')
    state = models.CharField(max_length=20, choices=STATE_CHOICES)
    location_description = models.TextField(blank=True, help_text="Specific island, village, or landmark info")
    
    # Geospatial data for mapping integrations
    latitude = models.DecimalField(max_digits=9, decimal_places=6, help_text="e.g. 6.9149")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, help_text="e.g. 158.1613")
    
    # Capacity Details
    capacity_details = models.TextField(help_text="Square footage, vessel maximums, or fleet metrics.")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPERATIONAL')
    
    # Contact Matrix
    contact_person = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=50, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['state', 'name']

    def __str__(self):
        return f"{self.name} - {self.get_state_display()}"




class DocumentRepository(models.Model):
    """Stores and indexifies uploads like DM Plans, Risk Profiles, and Regional Area Profiles"""
    CATEGORY_CHOICES = [
        ('DM_PLAN', 'Disaster Management Plan'),
        ('RISK_PROFILE', 'Risk Profile'),
        ('AREA_PROFILE', 'Area Profile'),
        ('ASSESSMENT TOOLS', 'Assessment Tools'),
    ]
    
    SUB_TYPE_CHOICES = [
        # Disaster Management Plans
        ('NDRP', 'National Disaster Response Plan'),
        ('SDRP', 'State Disaster Response Plan'),
        ('SOP', 'Standard Operating Procedure'),
        ('CONT', 'Contingency Plan'),
        ('EAP', 'Emergency Action Plan'),
        ('SECTOR', 'Sector Response Plan'),
        # Risk Profiles
        ('HAZARD', 'Hazard Profile'),
        ('CLIMATE', 'Climate Risk Assessment'),
        ('VULN', 'Vulnerability Analysis'),
        ('HISTORY', 'Historical Disaster Record'),
        ('STUDY', 'Risk Study'),
        # Assessment tools
        ('INITIAL DAMAGE ASSESSMENT','Initial Damage Assessment'),
    ]

    STATE_CHOICES = [
        ('NATIONAL', 'National / Federated Level'),
        ('CHUUK', 'Chuuk State'),
        ('KOSRAE', 'Kosrae State'),
        ('POHNPEI', 'Pohnpei State'),
        ('YAP', 'Yap State'),
    ]

    title = models.CharField(max_length=255, help_text="e.g. Chuuk State Disaster Response Plan Amendment")
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    sub_type = models.CharField(max_length=30, choices=SUB_TYPE_CHOICES)
    state = models.CharField(max_length=20, choices=STATE_CHOICES)
    
    # Secure storage vector pointing to 'media/drm_documents/' 
    file = models.FileField(
        upload_to='drm_documents/%Y/', 
        help_text="Upload official PDF, DOCX, or spatial analysis report sheets."
    )
    
    description = models.TextField(blank=True, help_text="Summary of scope, version rules, or operational triggers.")
    published_year = models.IntegerField(help_text="The year this policy or master document was enacted.")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_year', 'title']
        verbose_name = "DRM Strategic Document"
        verbose_name_plural = "DRM Strategic Documents"

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title} ({self.published_year})"