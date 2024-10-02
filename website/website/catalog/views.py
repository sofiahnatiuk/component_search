from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Component


class ComponentListView(ListView):
    model = Component
    template_name = 'catalog/index.html'  # Define your template
    context_object_name = 'components'
    paginate_by = 10  # Number of components per page