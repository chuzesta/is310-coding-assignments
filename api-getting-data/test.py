import requests
import apikey

apikey.save("THE_ONE_API_KEY", "LqNfy8PrdZbIg0FoFG8t")

the_one_api_key = apikey.load("THE_ONE_API_KEY")
authorization_headers = {
	'Authorization': 'Bearer ' + the_one_api_key
}
url = 'https://the-one-api.dev/v2/character?name=Galadriel'
response = requests.get(url, headers=authorization_headers)
galadriel_id = response.json()['docs'][0]['_id']
quote_url = f'https://the-one-api.dev/v2/character/{galadriel_id}/quote'
response = requests.get(quote_url, headers=authorization_headers)
print(response.json())