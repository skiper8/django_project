from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views import generic

from catalog.models import Products, Contacts, Blog, Version
from forms import ProductsForms, VersionForms


class ProductsListView(generic.ListView):
    model = Products
    form_class = ProductsForms

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('version_set')
        return queryset


class ProductsDetailView(generic.DetailView):
    model = Products
    form_class = ProductsForms


class ProductsCreateView(generic.CreateView):
    model = Products
    form_class = ProductsForms
    success_url = reverse_lazy('catalog:products_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Products, Version, form=VersionForms, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductsUpdateView(generic.UpdateView):
    model = Products
    form_class = ProductsForms
    success_url = reverse_lazy('catalog:products_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['formset'] = self._get_formset()
        return context_data

    def _get_formset(self):
        VersionFormset = inlineformset_factory(
            self.model, Version, form=VersionForms, extra=1
        )
        if self.request.method == 'POST':
            return VersionFormset(
                self.request.POST, instance=self.object
            )
        else:
            return VersionFormset(instance=self.object)

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductsDeleteView(generic.DeleteView):
    model = Products
    success_url = reverse_lazy('catalog:products_list')


class ContactsListView(generic.ListView):
    model = Contacts


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
    fields = ('title', 'text', 'image', 'is_active')
    success_url = reverse_lazy('catalog:blog_list')


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ('title', 'text', 'image', 'is_active')

    def get_success_url(self):
        return reverse('catalog:blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
