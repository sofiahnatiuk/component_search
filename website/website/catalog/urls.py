from django.urls import path

from .views import(
    ComponentListView, ComponentDetailView, CategoryDetailView, AboutView, report_component,
    report_list,
    toggle_report_read
)

urlpatterns = [
    path('', ComponentListView.as_view(), name='component-list'),
    path('component/<int:pk>/', ComponentDetailView.as_view(), name='component-detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('component/<int:component_id>/report/', report_component, name='report_component'),
    path('reports/', report_list, name='report_list'),
    path('reports/<int:report_id>/toggle/', toggle_report_read, name='toggle_report_read'),

]

