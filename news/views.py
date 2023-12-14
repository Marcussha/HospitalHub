from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import user_passes_test
from authrole.custom_context import user_is_admin, user_is_manager

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'admin/articles/show.html', {'articles': articles})

@user_passes_test(lambda u: user_is_admin(u) or user_is_manager(u), login_url='login')
def index(request):
    articles = Article.objects.all()
    return render(request, 'admin/articles/index.html', {'articles': articles})

def article_detail(request, id):
    article = Article.objects.get( id = id)
    return render(request, 'admin/articles/details.html', {'article': article})

@user_passes_test(lambda u: user_is_admin(u) or user_is_manager(u), login_url='login')
def add_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        pub_date = request.POST.get('pub_date')
        description = request.POST.get('description')
        
        try:
            new_article = Article.objects.create(
                title=title, 
                content=content, 
                pub_date=pub_date,
                description = description,
            ) 
            #return render(request, 'articles/create.html', {'new_article': new_article})
            return redirect('/news/index')
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return render(request, 'admin/articles/create.html', {'error_message': 'An error occurred while creating the article.'})
            
    articles = Article.objects.all()
    return render(request, 'admin/articles/create.html', {'articles': articles})

@user_passes_test(lambda u: user_is_admin(u) or user_is_manager(u), login_url='login')
def delete(request, id):
    article = Article.objects.get(id = id)
    article.delete()
    return redirect('/news/index')
            
