from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин HOME',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'About - О нас',
        'content': 'ABOUT - О нас',
        'text_on_page': 'Какой-то текст',
    }
    return render(request, 'main/about.html', context)
