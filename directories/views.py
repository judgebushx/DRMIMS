from django.views.generic import ListView
from .models import EmergencyContact
from .filters import EmergencyContactFilter

class DirectoryListView(ListView):
    model = EmergencyContact
    template_name = 'directories/directory_list.html'
    context_object_name = 'contacts'
    paginate_by = 25

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = EmergencyContactFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterform'] = self.filterset.form
        return context