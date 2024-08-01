from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contact

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contact),
]
