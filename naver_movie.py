# -*- coding: utf-8 -*- 

import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import csv
import re


base_url='https://movie.naver.com/movie/running/current.nhn?order=reserve'

response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

movie_info = soup.select('dt.tit')

for movie in movie_info:

    movie_data_schema={
        'movie_title':"",
        'movie_code':""
    }

    if isinstance(movie, NavigableString):
        continue
    if isinstance(movie, Tag):
        movie_data_schema['movie_title'] = movie.select_one('a').string
        movie_data_schema['movie_code'] = movie.select_one('a')['href']

    movie_data_schema['movie_code']=re.findall('\d+',movie_data_schema['movie_code'])[0]
    #print(movie_data_schema['movie_code'])
    with open('./naver_movie.csv','a') as csvfile:
        fieldnames = ['movie_title', 'movie_code']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)       
        csv_writer.writerow(movie_data_schema)
        

        print(movie_data_schema, '\n')


    
