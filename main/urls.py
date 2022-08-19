from django.urls import path
from .views import CategoryProductsView, ProductListView, ProductCategoryListView, ProductDetailView, CarouselListView, ProductImagesView
from . import views

urlpatterns = [
    path('order/<int:order_id>/pdf',
         views.admin_order_pdf,
         name='admin_order_pdf'),
    path('products', ProductListView.as_view(), name='products'),
    path('product/<slug:slug>',
         ProductDetailView.as_view(), name="product_detail"),
    path('product/images/<slug:slug>',
         ProductImagesView.as_view(), name="product_image"),
    path('category', ProductCategoryListView.as_view(), name='category'),
    path('category/<slug:slug>',
         CategoryProductsView.as_view(), name="category_product"),
         
    path('carousel', CarouselListView.as_view(), name="carousel")
]
