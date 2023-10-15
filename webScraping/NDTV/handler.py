from .NdtvNews import NdtvNews
from .helpers.ndtv_response import response

news_link = ["https://www.ndtv.com/latest",
             "https://www.ndtv.com/india",
             "https://www.ndtv.com/world",
             "https://www.ndtv.com/world-new",
             "https://www.ndtv.com/opinion",
             "https://www.ndtv.com/cities",
             "https://www.ndtv.com/education",
             "https://www.ndtv.com/offbeat",
             "https://www.ndtv.com/feature",
             "https://www.ndtv.com/science",
             "https://www.ndtv.com/people"]


def handler():
    ndtv = NdtvNews(news_link)
    get_response = ndtv.get_news()
    status = response(response_object=get_response)
    final_response = status.get_response()
    return final_response


