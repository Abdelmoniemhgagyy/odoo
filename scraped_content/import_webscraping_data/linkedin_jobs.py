from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import lxml

import json

options = Options()
driver = webdriver.Chrome(options=options)
job_title_search = "web developer"
country_search = "egypt"
url =f"https://eg.linkedin.com/jobs/search?keywords={job_title_search}&location={country_search}"
driver.get(url)
soup = BeautifulSoup(driver.page_source,"lxml")
cards_container = soup.find_all("div",{"class":"base-card"})
results = []
for i,job in enumerate(cards_container,1):
    job_title = job.find("h3",{"class":"base-search-card__title"}).text.strip()
    company = job.find("h4",{"class":"base-search-card__subtitle"}).text.strip()
    location = job.find("span",{"class":"job-search-card__location"}).text.strip()
    date = job.find("time",{"class":"job-search-card__listdate"})
    date_job = date.text.strip()  if date else "N/A"
    logo_tag = job.find("img",{"class":"artdeco-entity-image"})
    logo = logo_tag["data-delayed-url"] if logo_tag and logo_tag.has_attr("data-delayed-url") else None
    results.append({
        "id":i,
        "Job Title":job_title,
        "Company":company,
        "Location":location,
        "Date Job":date_job,
        "Logo":logo,
        "url":url
    })
with open("linkedin_jobs.json","w",encoding="utf-8") as f :
    json.dump(results,f,ensure_ascii=False,indent=5)
driver.quit()
