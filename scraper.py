import requests
from bs4 import BeautifulSoup as soup
from dateutil import parser

################################################
#                Scraper Class                 #
################################################

class Scraper:
    def __init__(self, url, websiteObjList):
        self.articleURL = url
        self.websiteObjList = websiteObjList
        self.articleTitle = ""
        self.articleBody = []
        self.articleDate = ""

        websiteName = url.split("www.")[1].split(".com")[0]

        for website in websiteObjList:
            if websiteName == website.getWebsiteName():
                self.website = website
                self.scrape()

    def scrape(self):
        print("[+] Scraping " + self.articleURL)
        page = requests.get(self.articleURL)
        soup_page = soup(page.content, 'html.parser')

        # scrape article title
        self.articleTitle = soup_page.find_all(self.website.getTitleTag())[0].get_text()

        # scape article body
        body = soup_page.find_all(self.website.getBodyTag())

        for line in body:
            self.articleBody.append(line.get_text())

        # scrape article publishing date
        date = soup_page.find_all(self.website.getPublishingDateTag())[0].get_text().strip()
        self.articleDate = self.normalizeDate(date)

    def normalizeDate(self, date):
        d = parser.parse(date)
        return d.strftime("%m/%d/%Y")

    def getArticleTitle(self):
        return self.articleTitle

    def getArticleDate(self):
        return self.articleDate

    def getArticleBody(self):
        return self.articleBody







