import re
import requests

regex_complier = re.compile('http://' + '([a-zA-Z]+.)*[a-zA-Z]+')

def download_text(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    raise Exception(f'Cannot open url: {url}')

def crawl(start_page, distance, action, visited_pages = []):
    if distance > 0 and start_page not in visited_pages:
        try:
            text = download_text(start_page)
            yield start_page, action(text)
            for url in set(url.group() for url in regex_complier.finditer(text)):
                for page, result in crawl(url, distance - 1, action, visited_pages + [start_page]):
                    yield page, result
        except Exception as e:
            print(e)

host = 'http://www.ii.uni.wroc.pl'
for url, wynik in crawl(host, 2, lambda tekst : 'Python' in tekst):
    print(f"{url}: {wynik}")
    