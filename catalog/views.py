from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from catalog.forms import ProductForm
from catalog.models import Category, Product


class BaseView:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'categories': Category.objects.filter(is_active=True),
            'logo': 'Tienda Virtual'
        })
        return context


class ProductListView(BaseView, ListView):
    model = Product

    def get_queryset(self):
        # select * from Product where is_active=True
        return Product.objects.filter(is_active=True)

    
class ProductDetailView(BaseView, DetailView):
    model = Product


class CategoryProductList(BaseView, ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(is_active=True, category=self.kwargs['pk'])


class ProductCreateView(BaseView, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
