from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse

from django.views.generic import (ListView, DetailView, TemplateView,
                                  CreateView, UpdateView, DeleteView)

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version, Category


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["versions"] = Version.objects.filter(is_version=True)
        return context



class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер для создания продукта
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        product = form.save()
        product.user = self.request.user
        product.save()
        return super().form_valid(form)


class ProductDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер для просмотра одного продукта
    """
    model = Product



class ProductUpdateView(LoginRequiredMixin, UpdateView):
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



    def get_form_class(self):
        user = self.request.user
        user.save()
        if user == self.object.user:
            return ProductForm
        if (user.has_perm('catalog.can_cancel_publication')
                and user.has_perm('catalog.can_change_description_product')
                and user.has_perm('catalog.can_change_category_product')):

            return ProductModeratorForm
        raise PermissionDenied



class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер для удаления продукта
    """
    model = Product
    success_url = reverse_lazy('catalog:home')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.user:
            return super().get_form_class()
        raise PermissionDenied


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'


class CategoryListView(LoginRequiredMixin, ListView):
    """
    Контроллер для просмотра списка категорий
    """
    context_object_name = 'categories'
    model = Category
    template_name = 'catalog/category_list.html'
