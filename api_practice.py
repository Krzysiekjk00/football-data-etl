import requests
import pandas as pd
from sqlalchemy import create_engine


url = "https://v3.football.api-sports.io/leagues"

payload = {}
headers = {
  'x-rapidapi-key': 'a34e68033cb8e0c68e0343cb3910f409',
  'x-rapidapi-host': 'v3.football.api-sports.io'
}

leagues = requests.request("GET", url, headers=headers, data=payload).json()['response']
country_leagues = []

for league in leagues:
    if league['country']['name'] != 'World':
        league_record = league['league']
        del league_record['logo']
        league_record['country'] = league['country']['name']
        country_leagues.append(league_record)

df = pd.DataFrame(country_leagues)
# print(type(df))



df.to_csv('country_leagues', sep=',', index=False, header=True)

engine = create_engine('postgresql://xxx:xxx@localhost:5432/xxx')
df.to_sql('country_football_leagues', engine, if_exists='replace')
