from django.contrib import admin
from django.urls import include, path
from .views import  SignUpView, userAccountView, userUpdateView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', SignUpView.as_view(), name='signUp' ),
    path('account/', userAccountView, name='account'),
    path('update/<int:id>', userUpdateView.as_view(),name='profile_update')
]