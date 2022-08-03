from django.shortcuts import render, redirect, get_object_or_404
from article_app.models import Article
from django.core.paginator import Paginator
from extensions.utils import jalali_converter


def all_articles(request):
    blogs = Article.objects.filter(allowing=True)
    pagination = Paginator(Article.objects.filter(allowing=True), 6)
    page = request.GET.get('page')
    blog = pagination.get_page(page)
    return render(request, 'article_app/article.html', context={'article': blogs, 'blog': blog})


def article_detail(request, id, slug):
    art = Article.objects.get(id=id, slug=slug)
    ip_address = request.user.ip_address
    if ip_address not in art.hits.all():
        art.hits.add(ip_address)
    return render(request, 'article_app/blog_detail.html', context={'article': art})
