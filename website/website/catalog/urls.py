from django.urls import path

from .views import ComponentListView, ComponentDetailView

urlpatterns = [
    path('', ComponentListView.as_view(), name='component-list'),
    path('component/<int:pk>/', ComponentDetailView.as_view(), name='component-detail'),
]

