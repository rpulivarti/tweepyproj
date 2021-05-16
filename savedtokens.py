import tweepy

import json

secrets_filename = 'tweepy.secret'
api_keys = {}
with open(secrets_filename, 'r') as f:
    api_keys = json.loads(f.read())

auth = tweepy.OAuthHandler(api_keys['consumer_key'], api_keys['consumer_secret'])
auth.set_access_token(api_keys['access_token'], api_keys['access_token_secret'])

api = tweepy.API(auth)
api.update_status('I did ita gain6!')

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

