from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Blog

class BlogListView(ListView):
    """
    Контроллер для отображения списка статей
    """
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_publication=True)
        return queryset
#

class BlogDetailView(DetailView):
    """
    Контроллер для отображения одной статьи
    """
    model = Blog

    # Функция для автоматического добавления количества просмотров
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object
#

class BlogCreateView(CreateView):
    """
    Контроллер для создания статьи
    """
    model = Blog
    fields = ('title', 'slug', 'content', 'image', 'created_at', 'is_publication', 'count_views')
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    """
    Контроллер для обновления статьи
    """
    model = Blog
    fields = ('title', 'slug', 'content', 'image', 'created_at', 'is_publication', 'count_views')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

#

class BlogDeleteView(DeleteView):
    """
    Контроллер для удаления статьи
    """
    model = Blog
    success_url = reverse_lazy('blog:blog_list')

