import requests
import string
import os
from bs4 import BeautifulSoup

url = 'https://www.nature.com/nature/articles?page='
link_url = 'https://www.nature.com'
intab = string.punctuation
outtab = ''
translator = str.maketrans('', '', string.punctuation)
number_of_pages = int(input())
type_of_article = input()
if type_of_article == 'Research Highlight':
    type_of_class = 'article-item__body'
elif type_of_article == 'News':
    type_of_class = 'article__body'

for i in range(1, number_of_pages):
    os.mkdir('Page_' + str(i))
    os.chdir('Page_' + str(i))
    r = requests.get(url + str(i), headers={ 'Accept-Language': 'en-US,en;q=0.5' })
    soup = BeautifulSoup(r.content, 'html.parser')
    articles = soup.find_all('article')
    article_titles = soup.find_all('a', { 'data-track-action': 'view article' })
    article_types = soup.find_all('span', { 'data-test': 'article.type' })
    links = []
    for link in article_titles:
        links.append(link.get('href'))
    for i in range(len(article_types)):
        if article_types[i].text.strip() == type_of_article:
            new_name = article_titles[i].text.strip()
            article_name = new_name.translate(translator).replace(" ", "_") + ".txt"
            new_file = open(article_name, 'wb')
            r1 = requests.get(link_url + links[i], headers={ 'Accept-Language': 'en-US,en;q=0.5' })
            soup1 = BeautifulSoup(r1.content, 'html.parser')
            # print(soup1.find('div', class_ = type_of_class).text.strip())
            #              soup1.find('div', class_='article__body').text.strip()
            new_file.write(soup1.find('div', class_= type_of_class).text.strip().encode())
            new_file.close()
    os.chdir('..')

print("Saved all articles.")
