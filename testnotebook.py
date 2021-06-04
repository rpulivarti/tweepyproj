# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
print("hi")


# %%
import tweepy


# %%
import json

secrets_filename = 'tweepy.secret'
api_keys = {}
with open(secrets_filename, 'r') as f:
    api_keys = json.loads(f.read())

auth = tweepy.OAuthHandler(api_keys['consumer_key'], api_keys['consumer_secret'])
auth.set_access_token(api_keys['access_token'], api_keys['access_token_secret'])


api = tweepy.API(auth)


# %%
public_tweets = api.home_timeline()


# %%
print(public_tweets[2])


# %%
import json

secrets_filename = 'tweepy.secret'
api_keys = {}
with open(secrets_filename, 'r') as f:
    api_keys = json.loads(f.read())

print(api_keys['access_token_secret'])


# %%



