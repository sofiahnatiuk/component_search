import requests
from bs4 import BeautifulSoup


def scrape_news():
    url = 'https://uea.kiev.ua/news/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'  # pretend to be a browser
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = []

    for article in soup.select('div.post-single'):
        title_tag = article.select_one('h2.post-title a')
        content_tag = article.select_one('div.post-content')
        image_tag = article.find('img')

        if not title_tag:
            continue

        title = title_tag.text.strip()
        link = title_tag['href']
        cover_image_url = image_tag['src'] if image_tag else ''

        # Get first paragraph inside the content div (if exists)
        thumbnail = ''
        if content_tag:
            first_p = content_tag.find('p')
            if first_p:
                thumbnail = first_p.text.strip()

        news_items.append({
            'title': title,
            'link': link,
            'thumbnail': thumbnail,
            'cover_image_url': cover_image_url,
        })

    return news_items
