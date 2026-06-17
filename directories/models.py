from django.db import models

class ContactSector(models.Model):
    """Classifies the sector (e.g., EOC, Health/Medical, Police/Fire, Utilities, International Partner)"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class EmergencyContact(models.Model):
    """Stores key operational nodes and human resources across the FSM DRM network"""
    STATE_CHOICES = [
        ('NATIONAL', 'National / Federated Level'),
        ('CHUUK', 'Chuuk State'),
        ('KOSRAE', 'Kosrae State'),
        ('POHNPEI', 'Pohnpei State'),
        ('YAP', 'Yap State'),
    ]

    agency_name = models.CharField(max_length=255, help_text="e.g. DECEM National EOC, Chuuk State Police")
    focal_person = models.CharField(max_length=255, blank=True, help_text="Specific person's name (Optional)")
    job_title = models.CharField(max_length=255, blank=True, help_text="e.g. Director, Task Force Commander")
    sector = models.ForeignKey(ContactSector, on_delete=models.PROTECT, related_name='contacts')
    state = models.CharField(max_length=20, choices=STATE_CHOICES)
    
    # Comms Grid
    primary_phone = models.CharField(max_length=100, help_text="Landline or primary satellite link number")
    secondary_phone = models.CharField(max_length=100, blank=True, help_text="Mobile, Radio Call Sign, or backup number")
    email = models.EmailField(blank=True)
    physical_address = models.TextField(blank=True)
    
    is_24_7_operational = models.BooleanField(default=False, verbose_name="24/7 Hotline Status")
    notes = models.TextField(blank=True, help_text="Radio frequencies, satellite dispatch codes, etc.")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['state', 'agency_name']
        verbose_name = "Emergency Contact"
        verbose_name_plural = "Emergency Contacts"

    def __str__(self):
        if self.focal_person:
            return f"{self.agency_name} - {self.focal_person} ({self.get_state_display()})"
        return f"{self.agency_name} ({self.get_state_display()})"