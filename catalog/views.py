from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(DetailView):
    model = Product