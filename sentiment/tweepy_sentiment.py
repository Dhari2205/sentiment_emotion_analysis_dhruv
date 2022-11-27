from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy
import numpy as np
import pandas as pd


def tweet_to_data_frame(tweets):
	df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
	return df


class Import_tweet_sentiment:

	def __init__(self):
		pass

	consumer_key="T6mvyDBxp7YY6BPeA62C6P6aK"
	consumer_secret="5k4CUgsWoVrwYdDRB19oLpEbEjKRDo1nd1phzRIVyz8wo4breo"
	access_token="938277833998299136-FiOMhdWOELXhDQZ4OD086v4k5tqE3Si"
	access_token_secret="VqQ2qneJkVeyVQVJWFiOlyQWY0a4rX79LDJ8gLwIL9tCP"

	def get_tweets(self, handle):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)

		account = handle
		item = auth_api.user_timeline(id=account,count=20)
		df = tweet_to_data_frame(item)

		all_tweets = []
		for j in range(20):
			all_tweets.append(df.loc[j]['Tweets'])
		return all_tweets

	def get_hashtag(self, hashtag):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)

		account = hashtag
		all_tweets = []

		for tweet in tweepy.Cursor(auth_api.search_tweets, q=account, lang='en').items(20):
			all_tweets.append(tweet.text)

		return all_tweets

