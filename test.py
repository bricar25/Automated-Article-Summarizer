import requests
from bs4 import BeautifulSoup

# Tells the program which website to scrape.
URL = "https://policyandpoliticsblog.com"

# Store response to GET request
page = requests.get(URL)

# 200 request indicates scrape was successful
# Checks if successful request
if page.status_code == 200:
    # If successful request, BeautifulSoup object created from scrape 
    soup = BeautifulSoup(page.content, 'html.parser')

    # Finds the <article> tag
    post = soup.find('article')

    if post:
        # Finds the <h2> tag, then extracts the title content.
        title = post.find('h2').get_text()

        # Finds the anchor tag, then extracts the URL content.
        article_url = post.find('a')['href']

        # Finds the <p> element, then extracts the entire article.
        text = post.find_all('p')

        print(title)
        print(article_url)
        print(text)
