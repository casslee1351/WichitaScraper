from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

rest_list = []
for x in range(1, 8):

    url = 'https://www.360wichita.com/Restaurants/'
    r = requests.get(url+str(x))
    soup = BeautifulSoup(r.content, 'html.parser')
    restaurants = soup.find_all('div', class_='tourBlockDetails')

    for restaurant in restaurants:
        name = restaurant.find('h2').text

        rest_dict = {
            'name': name
        }
        rest_list.append(rest_dict)
    time.sleep(5)

df = pd.DataFrame(rest_list)
df = df['name'].map(lambda x: str(x)[:-1])
df.to_excel("restaurants.xlsx", index=False)
