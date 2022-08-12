from django.urls import path
from .views import CategoryProductsView, ProductListView, ProductCategoryListView, ProductDetailView, CarouselListView, ProductImagesView
from . import views
urlpatterns = [
    path('order/<int:order_id>/pdf',
         views.admin_order_pdf,
         name='admin_order_pdf'),
    path('api/products', ProductListView.as_view(), name='products'),
    path('api/product/<slug:slug>',
         ProductDetailView.as_view(), name="product_detail"),
    path('api/product/images/<slug:slug>',
         ProductImagesView.as_view(), name="product_image"),
    path('api/category', ProductCategoryListView.as_view(), name='category'),
    path('api/category/<slug:slug>',
         CategoryProductsView.as_view(), name="category_product"),
    path('api/carousel', CarouselListView.as_view(), name="carousel")
]
