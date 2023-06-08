from django.urls import reverse_lazy, reverse
from django.views import generic

from catalog.models import Category, Products, Contacts, Blog


class ProductListView(generic.ListView):
    model = Products


class ContactsListView(generic.ListView):
    model = Contacts


class ProductDetailView(generic.DetailView):
    model = Products


class BlogListView(generic.ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset

class BlogDetailView(generic.DetailView):
    model = Blog

    def get_object(self, queryset=None):
        object = super().get_object(queryset=queryset)
        object.view_count += 1
        object.save()
        return object


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ('title', 'text', 'image', 'slug', 'is_active')
    success_url = reverse_lazy('catalog:blog_list')


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ('title', 'text', 'image', 'slug', 'is_active')

    def get_success_url(self):
        return reverse('catalog:blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
