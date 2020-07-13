from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.urls import reverse



# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form =  OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save( commit=False)
            order.user = request.user



            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()



            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],price = item['price'], quantity = item['quantity'])

                cart.clear()
                order_created.delay(order.id)
                request.session['order_id'] = order.id
                # return render(request, 'shop/order-created.html', {'order':order})
                return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request, 'shop/order.html' ,{'cart':cart, 'form':form})


