from django.db import models
from django.contrib.auth.models import User

class FAQCategory(models.Model):
    """Groups FAQ topics for organized directory indexing (e.g., Early Warning Systems, Post-Disaster Aid)"""
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, help_text="URL-friendly short name (e.g., early-warning-systems)")
    display_order = models.IntegerField(default=0, help_text="Determines layout sorting order (lower numbers bubble up)")

    class Meta:
        ordering = ['display_order', 'title']
        verbose_name = "FAQ Category"
        verbose_name_plural = "FAQ Categories"

    def __str__(self):
        return self.title

class FAQ(models.Model):
    """Stores validated operational questions and detailed Markdown-compatible answers"""
    category = models.ForeignKey(FAQCategory, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=255)
    answer = models.TextField(help_text="Provide clear, concise protocols. Supports standard line breaks.")
    is_published = models.BooleanField(default=True, help_text="Uncheck to temporarily hide from public view during legal/agency review")
    display_order = models.IntegerField(default=0, help_text="Controls order within its specific category")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'question']
        verbose_name = "Frequently Asked Question"
        verbose_name_plural = "Frequently Asked Questions"

    def __str__(self):
        return self.question




class BlogPost(models.Model):
    """Stores public disaster updates, climate newsletters, and active emergency declarations"""
    CATEGORY_CHOICES = [
        ('NOTICE', 'Community Notice'),
        ('PRESS_RELEASE', 'DECEM Press Release'),
        ('SITREP', 'Active Situation Report'),
        ('PREPAREDNESS', 'Safety & Preparedness Tips'),
    ]

    STATE_TAG_CHOICES = [
        ('ALL', 'All FSM States / National'),
        ('CHUUK', 'Chuuk State Focus'),
        ('KOSRAE', 'Kosrae State Focus'),
        ('POHNPEI', 'Pohnpei State Focus'),
        ('YAP', 'Yap State Focus'),
    ]

    title = models.CharField(max_length=255, help_text="e.g., FEMA Approves Compact Disaster Funding for Chuuk Recovery")
    slug = models.SlugField(max_length=255, unique=True, help_text="URL shortcut name (e.g., fema-approves-compact-disaster-funding)")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='NOTICE')
    state_tag = models.CharField(max_length=20, choices=STATE_TAG_CHOICES, default='ALL')
    
    summary = models.TextField(help_text="A short summary sentence displayed on the main blog page list cards.")
    content = models.TextField(help_text="The full text body of the news article. Supports standard line breaks.")
    
    # Optional image assignment for visual context
    featured_image = models.ImageField(
        upload_to='news_banners/%Y/', 
        blank=True, 
        null=True,
        help_text="Upload an image directly from your computer (JPEG/PNG)."
    )
    
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_published = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']
        verbose_name = "DRM News Post"
        verbose_name_plural = "DRM News Posts"

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"