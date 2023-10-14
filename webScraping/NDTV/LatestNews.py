import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

# https://ndtv.com/latest
def latest_news(news_link):
    response_news = []
    for ndtv_latest in news_link:
        try :
            res = requests.get(ndtv_latest)
            soup = BeautifulSoup(res.content, 'html.parser')
            logging.info(f"Called the NDTV API {ndtv_latest}")
            # dictionary format
            # news_dictionary = {
            #     "news": "NDTV",
            #     "links": ndtv_latest,
            #     "type": "",
            #     "headline": "",
            #     "content": [],
            #     "news_link": ""
            # }
            news_response = {}
            news = []
            # get the latest news
            for row in soup.find_all('div', attrs={'class': 's-ls_txt'}):
                for text in row.find_all('a'):
                    news_dictionary = {}
                    if text['href'] is not None:
                        content_response = get_content_by_url(text['href'])
                        news_dictionary['news'] = "NDTV"
                        news_dictionary['root_link'] = ndtv_latest
                        news_dictionary['headline'] = text.string
                        news_dictionary['content'] = content_response
                        news_dictionary['news_link'] = text['href']
                        news.append(news_dictionary)
            print(len(news))
            logging.info(f"Fetched {len(news)} news")
            news_response['link'] = ndtv_latest
            news_response['news'] = news
            response_news.append(news_response)

        except():
            pass;
    return response_news


def get_content_by_url(link):
    get_content = link
    resp = requests.get(get_content)
    soup = BeautifulSoup(resp.content, 'html.parser')
    article_published = soup.find('span', attrs={'itemprop': 'dateModified'})
    article_description = soup.find('h2', attrs={'class': 'sp-descp'})
    article_body = soup.find('div', attrs={'id': 'ins_storybody'})
    content_response = {
        "description": "",
        "content": [],
        "images": {"link": [],
                   "alt": []},
        "date": ""
    }
    contents = []
    images = []
    images_alt = []

    # date modified
    date = ""
    if article_published is not None :
        date = article_published.string
    # short description
    description = ""
    if article_description is not None:
        description = article_description.string
    # content
    if article_body is not None :
        for p_tag in article_body(['p']):
            if p_tag is not None:
                contents.append(p_tag.string)
        # image from the content
        for img in article_body.findAll('img', attrs={'id': 'story_image_main'}):
            if img is not None:
                images.append(img['src'])
                if img['alt'] is not None:
                    images_alt.append(img['alt'])
                else:
                    images_alt.append("")

    content_response['description'] = description
    content_response['content'] = contents
    content_response['images']['link'] = images
    content_response['images']['alt'] = images_alt
    content_response['date'] = date

    return content_response



