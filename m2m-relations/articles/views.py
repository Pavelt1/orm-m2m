from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article,Tags


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.prefetch_related("tags").all().order_by(ordering)
    for article in articles:
        article.sorted_tags = sorted(article.tags.all(), key=lambda tag: (not tag.is_main, tag.name))
    context = {"article" : articles}

    return render(request, template, context)
