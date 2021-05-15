from django.forms import ModelForm
from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'short_description',
            'large_description',
            'price',
            'quantity',
            'image'
        ]