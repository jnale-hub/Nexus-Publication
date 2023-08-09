from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from . import util


def index(request):

    context = {
        "articles": util.list_articles(),
    }
    return render(request, 'nexus_pub/index.html', context)


def view_article(request, id):
    articles = util.list_articles()
    article = None

    for a in articles:
        if a["id"] == id:
            article = a
            break

    if article is None:
        return render(request, 'article_not_found.html')

    related_articles = []
    for related_id in article.get("related_articles", []):
        for a in articles:
            if a["id"] == related_id:
                related_articles.append(a)
                break

    return render(request, 'nexus_pub/article.html', {'article': article, 'related_articles': related_articles})
