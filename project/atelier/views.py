from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    return render(request, 'main/index.html')



def home_view(request):
    user = request.user
    hello = 'Hello world'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/home.html', context)
    # return HttpResponse('Hello world')


def explore_view(request):
     return render(request, 'main/explore.html')


def art_view(request):
     return render(request, 'main/art.html')


def food_view(request):
     return render(request, 'main/food.html')


def craft_view(request):
     return render(request, 'main/craft.html')


def fashion_view(request):
     return render(request, 'main/fashion.html')


def illustration_view(request):
     return render(request, 'main/illustration.html')


def poetry_view(request):
     return render(request, 'main/poetry.html')


def dance_view(request):
     return render(request, 'main/dance.html')


def photography_view(request):
     return render(request, 'main/photography.html')


def music_view(request):
     return render(request, 'main/music.html')


def filming_view(request):
     return render(request, 'main/filming.html')


def about_view(request):
    return render(request, 'main/about.html')
