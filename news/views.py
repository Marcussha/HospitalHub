from django.shortcuts import render, get_object_or_404
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': articles})

def article_detail(request, id):
    article = Article.objects.get( id = id)
    return render(request, 'articles/details.html', {'article': article})
