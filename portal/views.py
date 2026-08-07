from django.shortcuts import render
from django.db import models
from django.views.generic import ListView, DetailView
from .models import FAQCategory, BlogPost
from repositories.models import LogisticsAsset, DocumentRepository
from directories.models import EmergencyContact

def home(request):
    """Serves an accessible public safety and disaster awareness portal"""
    
    # Query the 3 most recent published news bulletins/blog posts
    # Note: If your model uses a custom field name like 'created_at' or 'published_date', 
    # replace '-id' with your field name (e.g., '-created_at') to sort by date.
    recent_bulletins = BlogPost.objects.filter(is_published=True).order_by('-id')[:3]
    
    # Non-technical emergency response actions
    preparedness_steps = [
        {
            'title': '1. Know Your Risks',
            'desc': 'Identify if your home is vulnerable to high seas, landslides, or severe storm surges common during typhoon season.'
        },
        {
            'title': '2. Secure Fresh Water',
            'desc': 'Keep a minimum of 3 days of clean drinking water stored safely in sealed containers for every member of your family.'
        },
        {
            'title': '3. Monitor Radio Lines',
            'desc': 'Keep your battery-powered AM/FM radios tuned to local state broadcast stations for active emergency alerts.'
        },
    ]

    context = {
        'steps': preparedness_steps,
        'early_warning_system': 'https://example-fsm-alert.gov',
        'recent_bulletins': recent_bulletins,  # Passes data seamlessly to your home.html loop!
    }
    
    return render(request, 'portal/home.html', context)


class FAQListView(ListView):
    model = FAQCategory
    template_name = 'portal/faq.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return FAQCategory.objects.all().prefetch_related(
            models.Prefetch(
                'faqs',
                queryset=FAQCategory._meta.get_field('faqs').remote_field.model.objects.filter(is_published=True),
                to_attr='published_faqs'
            )
        )


class BlogNewsListView(ListView):
    """Renders the main news bulletin board with clean category filtering parameters"""
    model = BlogPost
    template_name = 'portal/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        queryset = BlogPost.objects.filter(is_published=True)
        category_filter = self.request.GET.get('category')
        if category_filter:
            queryset = queryset.filter(category=category_filter)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = self.request.GET.get('category', '')
        context['categories'] = BlogPost.CATEGORY_CHOICES
        return context


class BlogNewsDetailView(DetailView):
    """Renders a standalone clean layout for reading a specific public notice"""
    model = BlogPost
    template_name = 'portal/blog_detail.html'
    context_object_name = 'post'


def dashboards_view(request):
    """Renders the central Power BI analytics and monitoring catalog."""
    return render(request, 'portal/dashboards.html')