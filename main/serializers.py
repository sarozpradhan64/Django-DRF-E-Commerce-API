
from dataclasses import field
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Product, Product_category, Carousel, Product_image




class ProductSerializers(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    class Meta:
        model= Product
        exclude = ['cost_price',]
        lookup_field = 'slug'

    def get_thumbnail(self, Product):
        request = self.context.get('request')
        thumbnail = Product.thumbnail.url
        return request.build_absolute_uri(thumbnail)

class ProductCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model= Product_category
        fields ="__all__"
        lookup_field = 'slug'



# serializing both thumbnail and images for the carousel
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

