import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urljoin
from datetime import datetime
import datetime


base_url = 'https://www.privateequitywire.co.uk/'
pages = range(1, 2)


def private_equity_wire(date, pages):
    for i in pages:
        url = 'https://www.privateequitywire.co.uk/news'+'?page='+str(i)
        print(url)

        directory = str(date)
        parent_dir = "C:/Users/hamra/PycharmProjects/webscraping/Articles"
        path = os.path.join(parent_dir, directory)
        if os.path.isdir(path):
            pass
        else:
            os.mkdir(path)

        website_name = 'PrivateEquityWire'
        parent_dir = "C:/Users/hamra/PycharmProjects/webscraping/Articles/"+str(date)
        path = os.path.join(parent_dir, website_name)
        if os.path.isdir(path):
            pass
        else:
            os.mkdir(path)

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        part = soup.find('div',{'class': 'block-region-main'})
        article = part.find_all('article')


        news_urls = []
        for item in article:
            a_tags = item.find('a')
            clean_a_tags = a_tags['href']
            #print(clean_a_tags)
            news_url = urljoin(base_url,clean_a_tags)
            #print(news_url)
            news_urls.append(news_url)

        for link in news_urls:
            try:
                news_page = requests.get(link)
                soup = BeautifulSoup(news_page.content, 'html.parser')
                time_tags = soup.findAll('div', {'class': 'field-item'})
                clean_time = re.search(r'(?<=item">).*?(?= - )', str(time_tags)).group(0)
                clean_time = clean_time.replace("By Karin Wasteson | ", "")
                clean_time = clean_time.replace("By James Williams | ", "")
                clean_time = clean_time.replace("By Mark Kitchen | ", "")
                # print(clean_time)
                news_date = datetime.datetime.strptime(clean_time, "%d/%m/%Y").strftime('%d.%m.%Y')
                # print(news_date)
                headline = soup.find('h1').get_text()
                filename = headline.replace(r"—", "")
                filename = filename.replace(r"?", "")
                news_content_section = soup.find(class_='body field field-name-body field-label-hidden')
                news_paragraphs = news_content_section.findAll('p')
                news_content = []
                for item in news_paragraphs:
                    news_content.append(item.get_text(strip=True))
                news_content = ''.join(news_content)
                # print(news_content)
                if news_date == date:
                    with open(path+'/%s.txt' % filename, 'w') as f:
                        f.write(headline + str(news_content))
            except:
                pass


# =====================================================================================================================


def private_equity_wire_all(pages):
    for i in pages:
        url = 'https://www.privateequitywire.co.uk/news'+'?page='+str(i)
        print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        part = soup.find('div',{'class': 'block-region-main'})
        article = part.find_all('article')


        news_urls = []
        for item in article:
            a_tags = item.find('a')
            clean_a_tags = a_tags['href']
            #print(clean_a_tags)
            news_url = urljoin(base_url,clean_a_tags)
            #print(news_url)
            news_urls.append(news_url)

        for link in news_urls:
            try:
                news_page = requests.get(link)
                soup = BeautifulSoup(news_page.content, 'html.parser')
                time_tags = soup.findAll('div', {'class': 'field-item'})
                clean_time = re.search(r'(?<=item">).*?(?= - )', str(time_tags)).group(0)
                clean_time = clean_time.replace("By Karin Wasteson | ", "")
                clean_time = clean_time.replace("By James Williams | ", "")
                clean_time = clean_time.replace("By Mark Kitchen | ", "")
                # print(clean_time)
                news_date = datetime.datetime.strptime(clean_time, "%d/%m/%Y").strftime('%d.%m.%Y')
                # print(news_date)
                directory = str(news_date)
                parent_dir = "C:/Users/hamra/PycharmProjects/webscraping/Articles/All"
                path = os.path.join(parent_dir, directory)
                if os.path.isdir(path):
                    pass
                else:
                    os.mkdir(path)

                website_name = 'PrivateEquityWire'
                parent_dir = "C:/Users/hamra/PycharmProjects/webscraping/Articles/All/" + str(news_date)
                path = os.path.join(parent_dir, website_name)
                if os.path.isdir(path):
                    pass
                else:
                    os.mkdir(path)
                headline = soup.find('h1').get_text()
                filename = headline.replace(r"—", "")
                filename = filename.replace(r"?", "")
                news_content_section = soup.find(class_='body field field-name-body field-label-hidden')
                news_paragraphs = news_content_section.findAll('p')
                news_content = []
                for item in news_paragraphs:
                    news_content.append(item.get_text(strip=True))
                news_content = ''.join(news_content)
                # print(news_content)

                with open(path+'/%s.txt' % filename, 'w') as f:
                    f.write(headline + str(news_content))
            except:
                pass


# private_equity_wire('31.07.2020')
# private_equity_wire_all()
