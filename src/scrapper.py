''' Module contains Scrapper class used to scrape information from websites '''

import requests
from bs4 import BeautifulSoup
import datetime

import websites
from report_builder import ReportBuilder as rb


class Scrapper:

    @classmethod
    def scrape(cls):
        ''' Method scrapes the News, taken from BBC '''

        def news_scrape():
            ''' Method scrapes news report, outputing build news report '''
            try:
                soup = cls._get_soup(websites.NEWS_HEADLINE)
                headline_scrape = soup.findAll(
                    "h3", {"class": "gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text"})
                headline = headline_scrape[0].text

            except requests.exceptions.ConnectionError:
                return 'Internet lost - could not fetch from {}'.format(websites.NEWS_HEADLINE)
            except IndexError:
                return 'Could not fetch data from {}'.format(websites.NEWS_HEADLINE)
            else:
                return rb.build_news_report(
                    time=datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                    headline=headline
                )

        def weather_scrape():
            ''' Method scrapes weather report, outputing build weather report '''
            try:
                soup = cls._get_soup(websites.WEATHER_LONDON)
                weather_scrape = soup.findAll(
                    "div", {"class": "BNeawe iBp4i AP7Wnd"})
                weather = weather_scrape[0].text
            except requests.exceptions.ConnectionError:
                return 'Internet lost - could not fetch from {}'.format(websites.WEATHER_LONDON)
            except IndexError:
                return 'Could not fetch data from {}'.format(websites.WEATHER_LONDON)
            else:
                return rb.build_weather_report(
                    time=datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                    temperature=weather
                )

        return news_scrape(), weather_scrape()

    @classmethod
    def _get_soup(csl, url):
        ''' Private-like method returning soup for given url '''
        page = requests.get(url)
        return BeautifulSoup(page.content, 'html.parser')
