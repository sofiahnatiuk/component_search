from django.shortcuts import render
from .scraper import scrape_news


def news_list(request):
    news_items = scrape_news()
    return render(request, 'news/news_list.html', {'news_items': news_items})
