''' Module contains Scrapper class used to scrape information from websites '''

import requests
from bs4 import BeautifulSoup
import datetime

import websites
from report_builder import ReportBuilder.build_news_report

class Scrapper:

    @classmethod
    def scrape(cls):
        ''' Method scrapes the News, taken from BBC '''

        def news_scrape():
            soup = cls._get_soup(websites.NEWS_HEADLINE)
            headline_scrape = soup.findAll("h3", {"class": "gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text"})
            headline = headline_scrape[0].text

            return build_news_report(
                            time=datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                            headline=headline
                        )


        def weather_scrape():
            # TODO
            pass

        return news_scrape(), weather_scrape()


        

    @classmethod
    def _get_soup(csl, url):
        ''' Private-like method returning soup for given url ''' 
        page = requests.get(url)
        return BeautifulSoup(page.content, 'html.parser')
