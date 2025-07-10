from bs4 import BeautifulSoup
import requests
import lxml
import  json
url = "https://venturebeat.com/company/about/"
request = requests.get(url)
soup = BeautifulSoup(request.content,"lxml")
body = soup.find("div",class_="body-container")
title = body.find("h1",class_="entry-title").text.strip()
paragraphs=body.find_all("p",class_="p-rich_text_section")
content = "/n".join([p.text.strip() for p in paragraphs])
result = [{
            "title": title,
            "content": content ,
            "source_url": url,
            "status": "success" if request.content else "Failed"
        }]
with open("static_page.json","w",encoding="utf-8") as f :
    json.dump(result,f,ensure_ascii=False,indent=5)

