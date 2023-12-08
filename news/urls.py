from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('/details/<int:id>/', views.article_detail, name='article_detail'),
    path('/addnew', views.add_news, name="add_news"),
    path('/delete/<int:id>', views.delete, name="delete")
]
