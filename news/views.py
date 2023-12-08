from django.shortcuts import render, redirect
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': articles})

def article_detail(request, id):
    article = Article.objects.get( id = id)
    return render(request, 'articles/details.html', {'article': article})

def add_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        pub_date = request.POST.get('pub_date')
        
        try:
            new_article = Article.objects.create(
                title=title, 
                content=content, 
                pub_date=pub_date
            ) 
            #return render(request, 'articles/create.html', {'new_article': new_article})
            return redirect('/news')
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return render(request, 'articles/create.html', {'error_message': 'An error occurred while creating the article.'})
            
    articles = Article.objects.all()
    return render(request, 'articles/create.html', {'articles': articles})

def delete(request, id):
    article = Article.objects.get(id = id)
    article.delete()
    return redirect('/news')
            
