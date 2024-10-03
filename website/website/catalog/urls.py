from django.urls import path

from .views import ComponentListView

urlpatterns = [
    path('/', ComponentListView.as_view(), name='component-list'),
]

