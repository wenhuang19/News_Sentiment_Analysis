# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:52:53 2019

@author: User
"""

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import pandas as pd
import numpy as np
import newspaper
# to install newspaper for python3
# pip install newspaper3k
from newspaper import fulltext
from newspaper import Article

# getting urls from Google news feed
news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
# Print news title, url and publish date

news_df_columns = ['Site', 'url', 'news_title', 'news_text']
news_df = pd.DataFrame(columns=news_df_columns)

for news in news_list:
  print(news.title.text)
  print(news.link.text)
  print(news.pubDate.text)
  print("-"*60)

# get news body texts
news_df_columns = ['url', 'news_title', 'news_text', 'date']
news_df = pd.DataFrame(columns=news_df_columns)
for news in news_list:
    a= Article(news.link.text)
    a.download()
    a.parse()

    news_text = print('"{0}"'.format(a.text))
    print(news_text)
    # append to dataframe
    row = [news.link.text, news.title.text, news_text, news.pubDate.text]
    news_df.loc[len(news_df)] = row

# write to csv
news_df.to_csv('news.csv', sep=',', encoding='utf-8')




