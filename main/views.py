from django.shortcuts import get_object_or_404, render, redirect
# rest_framework views
from rest_framework import generics, permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, Product, Product_category, Carousel, Product_image
from .serializers import ProductCategorySerializers, ProductImageSerailizers, ProductSerializers, CarouselSerializers, ProductThumbnailSerializers

from django.conf import  settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import os
import weasyprint

from inertia import render


# redirect home page to the admin 
def redirect_admin(request):
    return redirect('admin/')


def home(request):
    return render(request, 'Index', props = {
        'events':['Django hello guys', 'testing django react']
    })

def login(request):
    name = 'Nanu Stores'
    return render(request, 'Login', props= {'events':[name], 'name':name} )


def admin_order_pdf(request, order_id):
    # return HttpResponse('tsex')
    # return render(request, "orders/pdf.html")
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/pdf.html', {'order':order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    return response




#------------------------------------------------------------------------------------------
# api views
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(state=True).order_by('-publish')
    serializer_class = ProductSerializers
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.order_by('-created')  # - means decending
    serializer_class = ProductSerializers
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class ProductCategoryListView(generics.ListAPIView):
    queryset = Product_category.objects.all()
    serializer_class = ProductCategorySerializers
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

# product with caterories
class CategoryProductsView(APIView):
    def get(self, request, slug=None, format=None):
        category = get_object_or_404(Product_category, slug = slug)
        queryset = Product.objects.order_by('-created').filter(category__exact = category)
        serializer = ProductSerializers(queryset, many = True)
        return Response(serializer.data)

class ProductImagesView(APIView):
    def get(self, request, slug=None, format=None):
        product = get_object_or_404(Product, slug=slug)
        queryset1= Product.objects.filter(id=product.id)
        queryset = Product_image.objects.filter(product__exact = product.id)
        serializer = ProductImageSerailizers(queryset, many = True, context={"request":request})
        serializer_2 = ProductThumbnailSerializers(queryset1, many=True, context={"request":request})
        serializer_list = [serializer.data, serializer_2.data]
        print(serializer_list)
        print("--------------")
        # print(serializer_2.data)
        content = {'status':1, 'responseCode':status.HTTP_200_OK, 'data':serializer_list}
        # print(content)
        return Response(content)

class CarouselListView(generics.ListAPIView):
    queryset = Carousel.objects.order_by('-created').filter(state=True)
    serializer_class = CarouselSerializers
    permission_classes = (permissions.AllowAny, )