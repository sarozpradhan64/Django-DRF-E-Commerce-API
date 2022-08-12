
from dataclasses import field
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Product, Product_category, Carousel, Product_image


class ProductSerializers(serializers.ModelSerializer):
    
    class Meta:
        model= Product
        exclude = ['cost_price',]
        lookup_field = 'slug'

class ProductCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model= Product_category
        fields ="__all__"
        lookup_field = 'slug'



class ProductThumbnailSerializers(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    class Meta:
        model = Product
        fields = ('thumbnail',)
        lookup_field = 'slug'

class ProductImageSerailizers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    class Meta:
        model = Product_image
        fields= "__all__"
        lookup_field='slug'
        
class CarouselSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = "__all__"

