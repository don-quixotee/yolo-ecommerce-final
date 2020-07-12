

# Register your models here.
from django.contrib import admin
from .models import Category, Product, ProductImage, Brand,  Review, Wishlist


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    class Meta:
        model = Category

admin.site.register(Brand)


class ProductImageAdmin(admin.StackedInline):
    model=ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageAdmin,]
    class Meta:
        model = Product

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Review)
admin.site.register(Wishlist)