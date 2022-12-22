"""atelier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import (home_view, explore_view, dance_view, photography_view, music_view, filming_view, art_view,
                    food_view, illustration_view, poetry_view, craft_view, fashion_view, index_view,
                    about_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index-view'),
    path('home/', home_view, name='home-view'),
    path('explore/', explore_view, name='explore-view'),
    path('about/', about_view, name='about-view'),
    path('photography/', photography_view, name='photography-view'),
    path('dance/', dance_view, name='dance-view'),
    path('music/', music_view, name='music-view'),
    path('filming/', filming_view, name='filming-view'),
    path('art/', art_view, name='art-view'),
    path('illustration/', illustration_view, name='illustration-view'),
    path('food/', food_view, name='food-view'),
    path('poetry/', poetry_view, name='poetry-view'),
    path('craft/', craft_view, name='craft-view'),
    path('fashion/', fashion_view, name='fashion-view'),
    
    
    path('accounts/', include('allauth.urls')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('blog/', include('blog.urls', namespace='blog')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
