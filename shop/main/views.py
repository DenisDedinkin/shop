from django.shortcuts import render

from goods.models import Category


def index(request):

    category = Category.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин HOME',
        'category': category,
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'About - О нас',
        'content': 'ABOUT - О нас',
        'text_on_page': 'Какой-то текст',
    }
    return render(request, 'main/about.html', context)
