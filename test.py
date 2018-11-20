from aylienapiclient import textapi

import secrets

client = textapi.Client(secrets.APP_KEY, secrets.APP_SECRET) 

# Sentiment from URL
s = client.Sentiment({'url':'https://twitter.com/donaldtrumpdbag/status/769196942631038976'})
print(s)

# Sentimet from text
s = client.Sentiment({'text': 'I am a stupid jackass'})
print(s)