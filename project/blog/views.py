from django.shortcuts import render
from .models import Blog
# Create your views here.

def shop_views(request):
    products = Blog.objects.all()


    context = {
        'products': products,
    }


    return render(request, 'blog/shop.html', context)
 