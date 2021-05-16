import tweepy
# This is a working 

import json

secrets_filename = 'tweepy.secret'
api_keys = {}
with open(secrets_filename, 'r') as f:
    api_keys = json.loads(f.read())


consumer_key = api_keys['consumer_key'] # Add your API key here
consumer_secret = api_keys['consumer_secret'] # Add your API secret key here


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')

print(redirect_url)

# Example w/o callback (desktop)
verifier = input('Verifier:')

try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print('Error! Failed to get access token.')


#auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

print("done")