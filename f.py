import requests 
import bs4
import json

data = []
mapping = {
    1: 'Authentic African Food',
    2: 'Nocturnal Life',
    3: 'Mbare Township',
    4: 'Ngomakurira Hike',
    5: 'Epworth',
    6: 'Craft And Curio Markets',
    7: 'Domboshava caves',
    8: "It's A Gango",
    9: 'Ummm Thirsty',
    10: 'Elephant Escapade',
    11: 'Horsing Around'
}

mapping = {mapping[key]: key for key in mapping}

resp = requests.get("http://localhost:8000/pricing/")
soup = bs4.BeautifulSoup(resp.content)

t = soup.find_all('table')[0]
rows = t.find_all('tr')
i = 21
for row in rows[4:]:
    cells = row.find_all('td')
    if len(cells) == 11:
        j = 1
        for price in cells[2:]:
            data.append({
                'model': 'app.priceschedule',
                'pk': i,
                'fields': {
                    'price': price.text.strip('$'),
                    'adventure': mapping[cells[0].text],
                    'participants': j
                }
            })
            i +=1 
            j +=1

with open('pricing.json', 'w') as fil:
    json.dump(data, fil)

