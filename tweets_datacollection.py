import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import date, timedelta

today = date.today()
five_years_ago = today - timedelta(days=5*365)

query = "indian politics lang:en -filter:retweets since:" + five_years_ago.strftime('%Y-%m-%d')
tweets = []
limit = 50

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content, tweet.likeCount, tweet.retweetCount])
        # print(len(tweets))
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet','Likes', 'Retweets'])
print(df)

# to save to csv
df.to_csv('tweets.csv')