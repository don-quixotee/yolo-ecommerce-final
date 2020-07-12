from django.shortcuts import render
from django.db.models import Q
from shop.models import Product
from django.views.generic import ListView

# Create your views here.



# class ProductListView(ListView):
#     model = Product
#     template_name = 'shop/products.html'
#     context_object_name = 'products'
#     pk_url_kwarg = 'id'


class ProductSearchListView(ListView):
    template_name='shop/products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query']=query
        return context

    def get_queryset(self):
        print(self.request.GET.get('q'))
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q',None)
        if query is not None:
            lookups =Q(name__icontains=query)| Q(description__icontains=query)
            return Product.objects.filter(lookups).distinct()
        return Product.objects.all()

    

