from django.urls import path

from .views import(
    ComponentListView, ComponentDetailView, CategoryDetailView, AboutView, report_component,
    report_list,
    toggle_report_read,
    ComponentCreateView,
    ComponentUpdateView,
    ComponentDeleteView,
)

urlpatterns = [
    path('', ComponentListView.as_view(), name='component-list'),
    path('component/<int:pk>/', ComponentDetailView.as_view(), name='component-detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('component/<int:component_id>/report/', report_component, name='report_component'),
    path('reports/', report_list, name='report_list'),
    path('reports/<int:report_id>/toggle/', toggle_report_read, name='toggle_report_read'),
    path('components/create/', ComponentCreateView.as_view(), name='component_create'),
    path('components/<int:pk>/edit/', ComponentUpdateView.as_view(), name='component_edit'),
    path('components/<int:pk>/delete/', ComponentDeleteView.as_view(), name='component_delete'),
]
