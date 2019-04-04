import csv
import tweepy
from textblob import TextBlob

consumer_key = "twitter consumer key" 
consumer_secret = "twitter consumer secret"

access_token = "twitter access token"
access_token_secret = "twitter access secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.search('nepal')


with open('sentiment.csv', mode='w', encoding='utf-8') as sentiment_file:
    sentiment_writer = csv.writer(sentiment_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    sentiment_writer.writerow(['Sentiment','Polarity', 'Subjetivity', 'Tweet'])
    for tweet in tweets:
    	analysis = TextBlob(tweet.text)
    	sentiment_writer.writerow(['positive' if analysis.sentiment.polarity >=0 else 'negative', analysis.sentiment.polarity, analysis.sentiment.subjectivity, tweet.text])
    