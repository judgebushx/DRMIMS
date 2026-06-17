from django.contrib import admin
from .models import FAQCategory, FAQ, BlogPost


@admin.register(FAQCategory)
class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'display_order', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('question', 'answer')
    list_editable = ('display_order', 'is_published')






@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'state_tag', 'is_published', 'published_date')
    list_filter = ('category', 'state_tag', 'is_published')
    search_fields = ('title', 'summary', 'content')
    prepopulated_fields = {'slug': ('title',)}  # Auto-writes standard URLs
    list_editable = ('is_published',)