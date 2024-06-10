from googlesearch import search
import requests
from bs4 import BeautifulSoup

def google_search_crawler(keyword, num_pages=5):
    urls = []
    for url in search(keyword, num=num_pages):
        urls.append(url)

    all_text = []
    for url in urls:
        try:
            response = requests.get(url, timeout=5, verify=False)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                texts = soup.stripped_strings
                all_text.append(' '.join(texts))
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    return all_text

if __name__ == "__main__":
    keyword = input(">> ")
    data = google_search_crawler(keyword)

    filename = "output.txt"

    with open(filename, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(item + "\n")

    print(f"Data saved to {filename}")
