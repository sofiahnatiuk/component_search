from django.urls import path

from .views import ComponentListView, ComponentDetailView, CategoryDetailView, AboutView

urlpatterns = [
    path('', ComponentListView.as_view(), name='component-list'),
    path('component/<int:pk>/', ComponentDetailView.as_view(), name='component-detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('about/', AboutView.as_view(), name='about'),
]

