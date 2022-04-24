import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import datetime
import os


base_url = 'https://www.reuters.com'
url = 'https://www.reuters.com/news/archive/privateEquity'

# pages = range(0,1)


def reuters(date, pages):
    for i in pages:
        url = 'https://www.reuters.com/news/archive/privateEquity?view=page&page='+str(i)+'&pageSize=10'
        print(url)

        directory = str(date)
        parent_dir = "C:/Users/hamra/PycharmProjects/webscraping/Articles"
        path = os.path.join(parent_dir, directory)
        if os.path.isdir(path):
            pass
        else:
            os.mkdir(path)

        website_name = 'Reuters'
        parent_dir = "C:/Users/hamra/PycharmProjects/webscraping/Articles/" + str(date)
        path = os.path.join(parent_dir, website_name)
        if os.path.isdir(path):
            pass
        else:
            os.mkdir(path)

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        part = soup.find(class_ = 'news-headline-list')
        top_news_section = part.find_all(class_= 'story-content' )
        top_news_urls = []
        for items in top_news_section:
            a_tags = items.find('a')
            # clean_sub_url = re.search(r'(?<=ref=").*?(?=")', str(a_tags)).group(0)
            href = a_tags['href']
            absolute_news_url = urljoin(base_url,href)
            top_news_urls.append(absolute_news_url)
            # print(absolute_news_url)

        for items in top_news_urls:
            try:
                page = requests.get(items)
                soup = BeautifulSoup(page.content, 'html.parser')
                time_tag = soup.find(class_='ArticleHeader_date')
                clean_time_tag = re.search(r'(?<=">).*?(?= /)', str(time_tag)).group(0)
                news_date = datetime.datetime.strptime(clean_time_tag, "%B %d, %Y").strftime('%d.%m.%Y')
                # print(news_date)
                if news_date == date:
                    headline = soup.find('h1').get_text()
                    filename = headline.replace(r"—", "")
                    filename = filename.replace(r"?", "")
                    news_content_section = soup.find(class_='StandardArticleBody_body')
                    news_paragraphs = news_content_section.findAll('p')
                    news_content = []
                    for paragraphs in news_paragraphs:
                        news_content.append(paragraphs.get_text(strip=True))
                    news_content = ''.join(news_content)
                    # print(headline)
                    # storage_client = storage.Client()
                    # bucket = storage_client.get_bucket(bucket_name)
                    # blob = bucket.blob(destination_folder_name + headline)
                    # blob.upload_from_string(news_content)
                    with open(path + '/%s.txt' % filename, 'w') as f:
                        f.write(headline + str(news_content))
            except:
                pass


# reuters('23.07.2020')

# ============================================Fetching All News========================================================
def reuters_all(pages):
    for i in pages:
        url = 'https://www.reuters.com/news/archive/privateEquity?view=page&page='+str(i)+'&pageSize=10'
        print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        part = soup.find(class_ = 'news-headline-list')
        top_news_section = part.find_all(class_= 'story-content' )
        top_news_urls = []
        for items in top_news_section:
            a_tags = items.find('a')
            # clean_sub_url = re.search(r'(?<=ref=").*?(?=")', str(a_tags)).group(0)
            href = a_tags['href']
            absolute_news_url = urljoin(base_url, href)
            top_news_urls.append(absolute_news_url)
            # print(absolute_news_url)

        for items in top_news_urls:
            try:
                page = requests.get(items)
                soup = BeautifulSoup(page.content, 'html.parser')
                time_tag = soup.find(class_='ArticleHeader_date')
                clean_time_tag = re.search(r'(?<=">).*?(?= /)', str(time_tag)).group(0)
                news_date = datetime.datetime.strptime(clean_time_tag, "%B %d, %Y").strftime('%d.%m.%Y')
                # print(news_date)
                directory = str(news_date)
                parent_dir = "C:/Users/hamra/PycharmProjects/webscraping/Articles/All"
                path = os.path.join(parent_dir, directory)
                if os.path.isdir(path):
                    pass
                else:
                    os.mkdir(path)
                website_name = 'Reuters'
                parent_dir = "C:/Users/hamra/PycharmProjects/webscraping/Articles/All/" + str(news_date)
                path = os.path.join(parent_dir, website_name)
                if os.path.isdir(path):
                    pass
                else:
                    os.mkdir(path)

                headline = soup.find('h1').get_text()
                filename = headline.replace(r"—", "")
                filename = filename.replace(r"?", "")
                news_content_section = soup.find(class_='StandardArticleBody_body')
                news_paragraphs = news_content_section.findAll('p')
                news_content = []
                for paragraphs in news_paragraphs:
                    news_content.append(paragraphs.get_text(strip=True))
                news_content = ''.join(news_content)
                with open(path + '/%s.txt' % filename, 'w') as f:
                    f.write(headline + str(news_content))
            except:
                pass


# reuters_all()
# reuters('31.07.2020')
