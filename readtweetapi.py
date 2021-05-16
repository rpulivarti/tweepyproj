import tweepy

import json

secrets_filename = 'tweepy.secret'
api_keys = {}
with open(secrets_filename, 'r') as f:
    api_keys = json.loads(f.read())


consumer_key = api_keys['consumer_key']  # Add your API key here
consumer_secret = api_keys['consumer_secret']
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
    print(tweet.text)