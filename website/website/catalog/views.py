from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Component

class ComponentDetailView(DetailView):
    model = Component
    template_name = 'catalog/detail.html'
    context_object_name = 'component'

class ComponentListView(ListView):
    model = Component
    template_name = 'catalog/index.html'
    context_object_name = 'components'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Component.objects.filter(
                Q(name__icontains=query) |
                Q(manufacturer__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            )
        return Component.objects.all()