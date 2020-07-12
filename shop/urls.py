
from django.urls import path

from .views  import HomeView, ProductDetailView, ProductListView, WishlistView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<int:id>/',ProductDetailView.as_view(), name='product-detail' ),
    path('products/', ProductListView.as_view(), name='productList'),
    path('category/<int:id>/', ProductListView.as_view(), name='product_by_category' ),
    path('product/add/<int:pk>/', WishlistView.as_view()  , name='add-wishlist'),
    path('wishlist/', WishlistView.as_view(), name='wishlist')
]
