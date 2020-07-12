
from django.urls import path

from  .views import ProductSearchListView


app_name = 'search'

urlpatterns = [
    path('', ProductSearchListView.as_view() , name='Query'),
 
]
