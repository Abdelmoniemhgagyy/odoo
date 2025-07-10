import json
from bs4 import BeautifulSoup
import requests
import lxml
import time

request = requests.get("https://techcrunch.com/")
soup = BeautifulSoup(request.content,"lxml")
news_container =soup.find_all("div",class_ = "wp-block-techcrunch-card wp-block-null")
results= []
for i,news in enumerate(news_container,1):
     title=news.find("h3",class_="loop-card__title").text.strip()

     author_tag = news.find("ul", class_="loop-card__meta-item loop-card__author-list")
     author = author_tag.text.strip() if author_tag else "No Author"

     publish_date_tag=news.find("time",class_="loop-card__meta-item")
     publish_date=publish_date_tag.text.strip() if publish_date_tag else " "

     news_url_tag = news.find("a",class_="loop-card__title-link")
     news_url = news_url_tag["data-destinationlink"] if news_url_tag and news_url_tag.has_attr("data-destinationlink") else None
     # news Page
     if news_url :
         request_news = requests.get(news_url)
         news = BeautifulSoup(request_news.content,"lxml")
         summary_tag =news.find("p",{"id":"speakable-summary"})
         summary =summary_tag.text.strip() if summary_tag else "No Summary"
         paragraphs = news.find_all("p",class_="wp-block-paragraph")
         full_content = "/n".join([p.text.strip() for p in paragraphs])
         time.sleep(2)
         results.append({
             "id": i,
             "Title": title,
             "author": author,
             "Publish Date": publish_date,
             "Summary":summary,
             "Full Content": full_content,
             "Source Url": news_url

         })
# create json file
with open("blog.json","w",encoding="utf-8") as f:
    json.dump(results,f,ensure_ascii=False,indent=3)
