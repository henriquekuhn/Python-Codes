from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
webpage_text = response.text

soup = BeautifulSoup(webpage_text, "html.parser")

# FIND THE FIRST
#articles = soup.find(class_="titleline")
#articles = articles.find(name="a")
#
#article_title = article_tag.getText()
#article_link = article_tag.get("href")
#article_upvote = soup.find(name="span", class_="score")

# FIND ALL
articles = soup.findAll(class_="titleline")
#articles = articles.findAll(name="a")

article_title = []
article_link = []
for tags in articles:
    tag = tags.find(name="a")  
    article_title.append(tag.getText()) 
    article_link.append(tag.get("href"))

article_upvote = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]
largest_point = max(article_upvote)
largest_index = article_upvote.index(largest_point)

#print(article_title)
#print(article_link)
print(article_upvote)
print(f"Thes most popular article is: {article_title[largest_index]}")
print(f"You can find at the link: {article_link[largest_index]}")