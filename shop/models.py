from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from froala_editor.fields import FroalaField
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation

 








# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to ='category/')
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Categoty'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse("model_detail", kwargs={"pk": self.pk})
        return reverse('shop:product_list_by_category',args=[self.slug])




class Brand(models.Model):
    name = models.CharField(max_length=100 , blank=True)
    discount = models.DecimalField(decimal_places=3, max_digits=10)


    def __str__(self):
        return self.name

    




class Product(models.Model):
    brand = models.ForeignKey(Brand , on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    slug = models.SlugField(max_length=250, db_index=True)
    description = models.TextField() 
    longDescription = FroalaField()
    stock = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to = 'product/')


    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse("product-detail", kwargs=[self.id, self.slug])



class ProductImage(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'product/')





class UserActionBase(models.Model):
    class Meta:
        abstract =True
    user = models.ForeignKey(get_user_model(), verbose_name="User", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name = 'Products' ,on_delete=models.CASCADE)




# class RatingModel(UserActionBase):
#     pass



class Review(UserActionBase):
    review = models.TextField(max_length=200)
    rating = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review





class Wishlist(UserActionBase):
    pass
