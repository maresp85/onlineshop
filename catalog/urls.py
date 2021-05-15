from django.urls import path

from catalog import views

app_name = 'catalog'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('categoria/<int:pk>/', views.CategoryProductList.as_view(), name='category_list'),
    path('crear/', views.ProductCreateView.as_view(), name='product_create')
]
