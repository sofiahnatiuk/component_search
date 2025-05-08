from django.shortcuts import render
from .scraper import scrape_news
from .models import NewsItem


def news_list(request):
    news_items = NewsItem.objects.order_by('-created_at')  # newest first
    return render(request, 'news/news_list.html', {'news_items': news_items})
