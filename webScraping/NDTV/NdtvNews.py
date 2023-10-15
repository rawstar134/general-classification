from .LatestNews import latest_news
from .LatestNews import page_content
class NdtvNews():
    def __init__(self,news_link):
        print("NDTV News Class")
        self.news_link = news_link

    def get_trending_news(self):
        return latest_news(self.news_link)
    def get_page_news(self):
        return page_content(self.news_link)



