# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 23:10:05 2019

@author: User
"""
import pandas as pd
import numpy as np
import newspaper
# to install newspaper for python3
# pip install newspaper3k
from newspaper import fulltext
from newspaper import Article

# getting some news articles from these 3 sites
cnn_paper = newspaper.build('http://cnn.com')
fox_paper = newspaper.build('http://fox.com')
reuter_paper = newspaper.build('http://reuters.com')

# Getting categories of the 3 news sites
for category in cnn_paper.category_urls():
        print(category)
        
for category in fox_paper.category_urls():
        print(category)
        
for category in reuter_paper.category_urls():
        print(category)


# focusing on U.S, url obtained from categories above
cnn_paper = newspaper.build('http://cnn.com/us')
fox_paper = newspaper.build('http://fox.com')
reuter_paper = newspaper.build('http://reuters.com')

# get text from the first 10 article of each source
        


news_df_columns = ['Site', 'url', 'news_title', 'news_text']
news_df = pd.DataFrame(columns=news_df_columns)
# process at most 10 articles from each source
max_article = 5


# load CNN article text
cnn_count = 0
for article in cnn_paper.articles:
    # article count ++
    cnn_count = cnn_count + 1
    
    # get article text
    a= Article(article.url)
    a.download()
    a.parse()
    
    print(article.url)
    
    # append to dataframe
    row = ["CNN", a.title, article.url, a.text]
    news_df.loc[len(news_df)] = row
    if(cnn_count > max_article):
        break
    
# load FOX article text
fox_count = 0
for article in fox_paper.articles:
    # article count ++
    fox_count = fox_count + 1
    
    # get article text
    a= Article(article.url)
    a.download()
    a.parse()
    
    # append to dataframe
    row = ["FOX", a.title, article.url, a.text]
    news_df.loc[len(news_df)] = row
    if(cnn_count > max_article):
        break
    
