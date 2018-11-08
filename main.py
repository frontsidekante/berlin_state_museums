from bs4 import BeautifulSoup
import requests
import website_list

root_url = 'https://www.smb.museum/'
all_exc_url = root_url+'museen-und-einrichtungen/museum-fuer-fotografie/ausstellungen/aktuell.html'

r = requests.get(all_exc_url)
soup = BeautifulSoup(r.content, 'html.parser')

complete_exc_data = {}

for link in soup.find_all('h4'):
    exc_data = {}
    exc_data["mus_name"] = link.find(text=True, recursive=False)

    children = link.findChildren("a", recursive=False)
    for child in children:
        exc_data["exc_name"] = child.text
        exc_data["exc_url"] = root_url+child.get("href")

print(exc_data)
