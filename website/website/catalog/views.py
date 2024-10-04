from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
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
    paginate_by = 10  # Number of components per page