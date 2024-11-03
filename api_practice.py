import requests
import pandas as pd

url = "https://v3.football.api-sports.io/leagues"

payload = {}
headers = {
  'x-rapidapi-key': 'a34e68033cb8e0c68e0343cb3910f409',
  'x-rapidapi-host': 'v3.football.api-sports.io'
}

leagues = requests.request("GET", url, headers=headers, data=payload).json()['response']

polish_leagues = []

for league in leagues:
    if league['country']['name'] == 'Poland':
        polish_leagues.append(league['league'])

df = pd.DataFrame(polish_leagues)
df.to_csv('polish_football_leagues', sep=',', index=False, header=True)

