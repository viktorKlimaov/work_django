from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse

from django.views.generic import (ListView, DetailView, TemplateView,
                                  CreateView, UpdateView, DeleteView)

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["versions"] = Version.objects.filter(is_version=True)
        return context



class ProductCreateView(CreateView):
    """
    Контроллер для создания продукта
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductDetailView(DetailView):
    """
    Контроллер для просмотра одного продукта
    """
    model = Product



class ProductUpdateView(UpdateView):
    """
    Контроллер для обновления продукта
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        FormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        context_data['formset'] = FormSet

        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))



class ProductDeleteView(DeleteView):
    """
    Контроллер для удаления продукта
    """
    model = Product
    success_url = reverse_lazy('catalog:home')


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'
