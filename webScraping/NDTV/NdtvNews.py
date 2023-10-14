from .LatestNews import latest_news
class NdtvNews():
    def __init__(self,news_link):
        print("NDTV News Class")
        self.news_link = news_link

    def get_news(self):
        return latest_news(self.news_link)



