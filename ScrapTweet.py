import pandas as pd
from ntscraper import Nitter

scraper = Nitter()

tweets = scraper.get_tweets("ARanganathan72",mode='user',number=5)

result = []
for tweet in tweets['tweets']:
  data = [tweet['text']]
  result.append(data)
print(result)

