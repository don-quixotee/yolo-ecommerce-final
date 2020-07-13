from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import FormMixin
from .models import Product, ProductImage, Category, Review, Wishlist
from cart.forms import CartAddProductForm
from .forms import ReviewForm
from  django.db.models import Avg
from django.contrib import auth
from django.http import HttpResponseRedirect
from recommendations.recommender import Recommender





# Create your views here.

class HomeView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/product_list.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        category = Category.objects.all()
        context['category']=category
        return context
    def get_queryset(self):
        return Product.objects.all()[:4]


class ProductDetailView(FormMixin, DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'shop/product_detail.html'
    pk_url_kwarg = 'id'
    form_class = ReviewForm

    def get_success_url(self):
        return  reverse('product-detail', kwargs={'id':self.object.id})

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()
        context['cart_product_form']= cart_product_form
        product = self.get_object()
        pic = ProductImage.objects.filter(product=product)
        context['pictures']=pic
        productReview = Review.objects.filter(product=product).order_by('-rating')[:3]
        avg_rating = productReview.aggregate(Avg('rating'))
        context['avg_rating'] = avg_rating.get('rating__avg')
        context['productReview'] = productReview
        r_count = Review.objects.filter(product=product).count()
        context['r_count']=r_count
        r = Recommender()

        recommended_products  = r.suggest_products_for([product], 4)
        context['recommendations']=recommended_products

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        print(form)
        if form.is_valid():
            product = self.get_object()
            new_review = form.save(commit=False)
            new_review.product = product
            new_review.user = self.request.user
            new_review.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    


# class ProductCategoryView(DetailView):
#     model = Category
#     context_object_name = 'products'
#     template_name='shop/category.html'
#     pk_url_kwarg ='id'

#     def get_context_data(self,**kwargs):
#         context= super().get_context_data(**kwargs)
#         category = self.get_object()
#         products = Product.objects.filter(category=category)
#         context['products']=products
#         return context




class ProductListView(ListView):
    model = Product
    template_name = 'shop/products.html'
    context_object_name = 'products'
    pk_url_kwarg = 'id'

    def get(self, request, id=None):
        product = Product.objects.all()
        category = Category.objects.all()


        if id:
            cat =Category.objects.get(id=id)
            product = Product.objects.filter(category=cat)
        context = {'products':product, 'category':category}
        return render(request, 'shop/products.html', context)


class WishlistView(ListView):
    model = Wishlist
    template_name = 'shop/wishlist.html'
    context_object_name = 'products'


    def get_success_url(self):
        return reverse_lazy('wishlist')
    
    def get(self, request, pk=None):
        if pk:
            user = auth.get_user(request)
            wishlist, created = self.model.objects.get_or_create(user=user, product_id=pk)
            wishlist.user = user

            if not created:
                wishlist.delete()

            wishlist.save()

            user = self.request.user
            user_id = user.id
            products = Wishlist.objects.filter(user=user_id)
            return render(request, 'shop/wishlist.html', {'products':products})
        


        user = self.request.user
        user_id = user.id
        products = Wishlist.objects.filter(user=user_id)
        return render(request, 'shop/wishlist.html', {'products':products})
        

        





    