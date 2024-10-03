from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ComponentListView

urlpatterns = [
    path('index/', ComponentListView.as_view(), name='component-list'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
