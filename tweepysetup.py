import re
import tweepy
import requests

session = requests.Session()

consumer_key = "hCs9rMJUIvVBoYoJtyPmV69kb"  # Add your API key here
consumer_secret = "Yy4wKRT6VWK4y0nByu4nXGzydGTvB5iN1oZcw84zKX9H9oiQfJ"  # Add your API secret key here

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')


# Example w/o callback (desktop)
verifier = input('Verifier:')