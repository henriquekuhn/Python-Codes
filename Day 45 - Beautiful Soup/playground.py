from bs4 import BeautifulSoup
import os
import lxml

DIR = os.getcwd() + "/Day 45 - Beautiful Soup"
os.chdir(DIR)

with open("website.html", 'r', encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")
print(soup.title.string)

all_anchor_tags = soup.findAll(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print("-----")
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

id_select = soup.select_one("#name")
print(id_select)

class_select = soup.select(".heading")
print(class_select)