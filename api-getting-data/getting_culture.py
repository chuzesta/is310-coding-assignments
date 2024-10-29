import requests
import apikey
import pandas as pd
import os
import pyeuropeana.apis as apis
import pyeuropeana.utils as utils
apikey.save("EUROPEANA_API_KEY", "INSERT_YOUR_API_KEY_HERE")
europeana_api_key = apikey.load("EUROPEANA_API_KEY")
os.environ['EUROPEANA_API_KEY'] = europeana_api_key
import discogs_client
d = discogs_client.Client('UIUC_IS310_JFANG/0.1', user_token="INSERT DISCOGS USER TOKEN")
results = d.search('The invention of animals', type='release')
print(results[1])
data = {
    'Artist': results[1].artists[0].name,
    'Album': results[1].title,
    'Genres': results[1].genres,
    'Label': results[1].labels,
    'Styles': results[1].styles,
    'Year': results[1].year,
    'Country': results[1].country,
    'Format': results[1].formats,
    'Tracklist': [results[1].tracklist],
    'Credits': [],
    "Stats": results[1].marketplace_stats,
}
for i in results[1].credits:
    if i.name not in data['Credits']:
        data['Credits'].append(i.name)
df = pd.DataFrame([data])
df.to_csv('discogs-api-items.csv', index=False)

result = apis.search(query="Free Improvisation", TYPE = "concept") # Genre was free jazz
df2 = utils.search2df(result)
df2.to_csv('europeana-api-items.csv', index=False)
