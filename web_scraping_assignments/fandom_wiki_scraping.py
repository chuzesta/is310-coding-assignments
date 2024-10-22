import time
import requests
from bs4 import BeautifulSoup
import re
import json
alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "¡"]
url = "https://adventuretime.fandom.com/wiki/Category:Characters?from="
main = "https://adventuretime.fandom.com"

character_data = []
character_info = []

def get_character_links(letter):
    response = requests.get(url+letter)
    soup = BeautifulSoup(response.text, "html.parser")
    temp = soup.find_all('a', class_='category-page__member-link')
    for char in temp:
        character_links = {"character": char.get_text().strip(), "character_link": char.get('href')}
        character_data.append(character_links)


def get_character_info(dict):
    response1 = requests.get(main+dict['character_link'])
    soup = BeautifulSoup(response1.text, "html.parser")
    #print(soup.prettify())
    infobox = soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color')
    character_wrapper = []
    for item in infobox:
        character_attribute = {"attribute": item.find('h3', class_='pi-data-label pi-secondary-font').get_text().strip(), "value": item.find('div', class_='pi-data-value pi-font').get_text().strip()}
        character_wrapper.append(character_attribute)
    character_info.append(character_wrapper)
    print(character_wrapper)


for a in alph:
    get_character_links(a)
#print(character_data)
for i in character_data:
    get_character_info(i)
print(character_info)

with open('character_info.json', 'w') as json_file:
    json.dump(character_info, json_file, indent=4)