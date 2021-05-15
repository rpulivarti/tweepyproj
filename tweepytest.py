import tweepy

consumer_key = "hCs9rMJUIvVBoYoJtyPmV69kb"  # Add your API key here
consumer_secret = "Yy4wKRT6VWK4y0nByu4nXGzydGTvB5iN1oZcw84zKX9H9oiQfJ"  # Add your API secret key here
access_token = "389753213520392195-18qyVhnPW712NEY1l5IfOLQwMnEcbO"
access_token_secret = "MwghCxDqE6xTJagpOe0SA1Vg3zxmgfk60DvKUM99TLN0d"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)