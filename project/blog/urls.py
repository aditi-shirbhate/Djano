from django.urls import path
from .views import shop_views

app_name = 'blog'

urlpatterns = [

    path('', shop_views, name='shop-view')
]
