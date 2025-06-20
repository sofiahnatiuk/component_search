from django.urls import path

from .views import(
    ComponentListView,
    ComponentDetailView,
    CategoryDetailView,
    AboutView,
    report_component,
    report_list,
    toggle_report_read,
    ComponentCreateView,
    ComponentUpdateView,
    ComponentDeleteView,
    CategoryTreeView,
    CategoryCreateView,
    CategoryDeleteView,
    CategoryUpdateView,
    FavoriteComponentListView,
    add_to_favorites,
    remove_from_favorites,
    ComponentCompareView,
    AddToCompareView,
    RemoveFromCompareView,
)

urlpatterns = [
    path('', ComponentListView.as_view(), name='component-list'),
    path('component/<int:pk>/', ComponentDetailView.as_view(), name='component-detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/add/', CategoryCreateView.as_view(), name='category-add'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category-edit'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('about/', AboutView.as_view(), name='about'),
    path('component/<int:component_id>/report/', report_component, name='report_component'),
    path('reports/', report_list, name='report_list'),
    path('reports/<int:report_id>/toggle/', toggle_report_read, name='toggle_report_read'),
    path('components/create/', ComponentCreateView.as_view(), name='component_create'),
    path('components/<int:pk>/edit/', ComponentUpdateView.as_view(), name='component_edit'),
    path('components/<int:pk>/delete/', ComponentDeleteView.as_view(), name='component_delete'),
    path('categories/tree/', CategoryTreeView.as_view(), name='category_tree'),
    path('favorites/', FavoriteComponentListView.as_view(), name='favorites'),
    path('favorites/add/<int:pk>/', add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/<int:pk>/', remove_from_favorites, name='remove_from_favorites'),
    path('compare/', ComponentCompareView.as_view(), name='compare'),
    path('compare/add/<int:pk>/', AddToCompareView.as_view(), name='add_to_compare'),
    path('compare/remove/<int:pk>/', RemoveFromCompareView.as_view(), name='remove_from_compare'),
]
