from bs4 import BeautifulSoup
import requests
import website_list

root_url = 'https://www.smb.museum/'
all_exh_url = root_url+'museen-und-einrichtungen/museum-fuer-fotografie/ausstellungen/aktuell.html'

r = requests.get(all_exh_url)
soup = BeautifulSoup(r.content, 'html.parser')

complete_exh_data = {}

for link in soup.find_all('h4'):
    exh_data = {}
    exh_data["mus_name"] = link.find(text=True, recursive=False)

    children = link.findChildren("a", recursive=False)
    for child in children:
        exh_data["exh_name"] = child.text
        exh_data["exh_url"] = root_url+child.get("href")

print(exh_data)
