import requests
from lxml import etree
import json

url = 'https://movie.douban.com/j/search_subjects'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
parameters ={'type':'tv','tag':'热门','sort':'recommend','page_limit':20,'page_start':0}
# 加上header参数可以伪造浏览器，实现反反爬
resp = requests.get(url, params = parameters, headers = headers)
respString = resp.text
# respString = resp.content
# respString = resp.json()
print(respString)

def saveToFile(x):
    with open("movie.txt",'w',encoding='UTF-8') as file:
        file.write(x)

respDict = json.loads(respString)
lists = respDict["subjects"]
movieName = {}
for item in lists:
    title = item["title"]
    movieName.update({"电影名":title})
    print(title)

movieNameString = json.dumps(movieName,ensure_ascii=False)
saveToFile(movieNameString)