import tweepy
from textblob import TextBlob 

consumer_key = "tEdvNAY2zbwvRpunL8b6NZ9Fi"
consumer_secret = "e0w6WTwjzVBhlbW7DJ8Y6mWXHMsTQIE9WAsq8cdjdgpxyBGfwo"

access_token = "1394326038-Ss1gnEPaMGMN2AVuvtz81oVT9hjn0QxosEjVQbE"
access_secret = "Qey67q8OaKaStml9FjazGTbz8jQZFlISkhov9sMgTdhV9"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

sentiment_analysis_txt = open('sentiment.txt', 'w')
public_tweets = api.search('Berger to Ajah')
text = ""
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

sentiment_analysis_txt.write(text)
sentiment_analysis_txt.close()
