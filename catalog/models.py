from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField


class Category(models.Model):
    name = models.CharField(max_length=48, unique=True, verbose_name='nombre')

    is_active = models.BooleanField(default=True, verbose_name='está activa')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='categoria')

    name = models.CharField(max_length=128, verbose_name='nombre')
    
    short_description = models.TextField(max_length=128, verbose_name='descripción corta')

    large_description = models.TextField(max_length=480, verbose_name='descripción larga')

    price = models.IntegerField(verbose_name='precio') 

    quantity = models.IntegerField(verbose_name='cantidad')

    is_active = models.BooleanField(default=True, verbose_name='está activo')

    image = models.ImageField(verbose_name='imagen', upload_to='products')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')

    def __str__(self):
        return f'{self.name} - {self.price} - {self.category}'

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'


class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='product')

    image = models.ImageField(verbose_name='imagen', upload_to='products_detail')

    class Meta:
        verbose_name = 'imagen del producto'
        verbose_name_plural = 'imagen de los productos'