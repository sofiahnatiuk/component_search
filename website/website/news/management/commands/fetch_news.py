from django.core.management.base import BaseCommand
from news.scraper import scrape_news


class Command(BaseCommand):
    help = 'Scrape news from uea.kiev.ua and save new items to the database'

    def handle(self, *args, **options):
        self.stdout.write("Scraping and saving news...")
        scrape_news()
        self.stdout.write(self.style.SUCCESS("News scraping complete."))
