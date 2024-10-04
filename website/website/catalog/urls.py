from django.urls import path

from .views import ComponentListView, ComponentDetailView, CategoryDetailView

urlpatterns = [
    path('', ComponentListView.as_view(), name='component-list'),
    path('component/<int:pk>/', ComponentDetailView.as_view(), name='component-detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),  # Add this line
]

