import requests
from bs4 import BeautifulSoup
response = requests.get('https://news.ycombinator.com/')

text = response.text

soup = BeautifulSoup(text, 'html.parser')
# prettified = soup.prettify()
# print(prettified)
# print(soup.title.string)

articles = soup.select('span.titleline a')

ariticle_text = []
article_links = []
for article in articles:
    article_links.append(article.get('href'))
    ariticle_text.append(article.get_text())
# print(ariticle_text)
# print(article_links)
upvotes = []
for upvote in soup.select("span.subline span.score"):
    upvotes.append(int(upvote.get_text().split()[0]))
# print(upvotes)
import numpy as np
upvotes = np.array(upvotes)
i = upvotes.argmax()
# print(len(ariticle_text))
# print(len(article_links))
# print(len(upvotes))
# print(i)
print(ariticle_text[i],article_links[i],upvotes[i],"votes",i+1)
