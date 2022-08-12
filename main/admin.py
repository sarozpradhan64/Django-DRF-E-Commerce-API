from django.contrib import admin
from .models import Product, Product_category, Product_image, Carousel, Order, OrderItem
from django.urls import reverse
from django.utils.safestring import mark_safe
# Register your models here.


class ProductCategoryAdmin(admin.ModelAdmin):
    class Meta:
        Product_category
    prepopulated_fields = {'slug': ('title',)}


class ProductImageInline(admin.TabularInline):
    model = Product_image


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]
    list_display = ('id', 'title', 'marked_price', 'category', 'status', 'state')
    list_filter = ('category', 'status')
    exclude = ('review', 'rating')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('status', 'state')


class CarouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'state', 'image')


class OrderItemInline(admin.TabularInline):
     model = OrderItem
     raw_id_fields = ['product']

def order_pdf(obj):
        url = reverse('admin_order_pdf', args=[obj.id])
        return mark_safe(f'<a href="{url}">PDF</a>')
order_pdf.short_description = 'Invoice'

class OrderAdmin(admin.ModelAdmin):

    list_display = ['id', 'c_name', 'c_email','c_phone',
                    'c_address', 'paid', order_pdf,
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
 


admin.site.register(Carousel, CarouseAdmin)
admin.site.register(Product_category, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)