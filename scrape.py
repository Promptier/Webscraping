from datetime import datetime
from pprint import pprint
import requests, re, json
from bs4 import BeautifulSoup as bs

today = datetime.now().strftime('%m-%d-%Y')
urls = {
    'Svelte': 'https://github.com/sveltejs/svelte',
    'React': 'https://github.com/facebook/react',
    'Angular': 'https://github.com/angular/angular'
}

def get_stars(url):
    r = requests.get(url)
    soup = bs(r.text,'html.parser')

    mt_el = soup.find_all('div',class_="mt-2")
    tmp_list = []
    for i, e in enumerate(mt_el):
        tmp_list.append(mt_el[i].text.strip())

    for e in tmp_list:
        if "stars" in e:
           match = re.search(r'(\d{1,4}\.\d+|\d{1,4})',e)
           star = match.group() 

    return star

data = {}
data[today] = {}
for name, url in urls.items():
    stars = get_stars(url)
    data[today][name] = float(stars) if '.' in stars else int(stars)

with open("data.json", "a") as f:
    json.dump(data, f, indent=4)
