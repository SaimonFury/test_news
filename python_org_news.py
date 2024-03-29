import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False

def get_python_news(html):
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_news = soup.find("ul", class_= "list-recent-posts").findAll("li")
        result_news = []
        for news in all_news:
            title = news.find("a").text
            url = news.find("a")["href"]
            published = news.find("time").text
            result_news.append({
                "title": title,
                "url": url,
                "published": published
            })
        return result_news
    return False
  
    # for link in soup.find_all("a"): парсит все ссылки
    #     print(link.get("href"))

if __name__ == "__main__":
    html = get_html("https://www.python.org/blogs/")
    if html:
        # with open('python_org_news.html', 'w', encoding = 'utf8') as f:
        #     f.write(html)
        news = get_python_news(html)
        print(news)
