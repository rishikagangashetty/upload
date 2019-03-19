import tweepy
import time
import datetime

ACCESS_TOKEN = '1107629035117596672-kHjrpTe6slTDzub0YgxqmktJuyzA1S'
ACCESS_SECRET = 'sLE2lEBPEzmr7Xyx8aLHqerVT9uYHPSgKVSv91HSBUZll'
CONSUMER_KEY = 'HploXoH1P2bKZdR3MHmxKzGK0'
CONSUMER_SECRET = 'fhhHr6zs2YthPLQhmstRoTLgvsUhU62rY3Sjirwsq3ToxSY21e'
SEARCH=input("Enter the search string ")
FROM=str('2016-01-01')
TO=str('2019-01-01')
INPUT_FILE_PATH= './'+SEARCH+'.txt'

num=int(input("Enter the number of tweets you want to retrieve for the search string "))
auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

i=0
f = open(INPUT_FILE_PATH, 'w', encoding='utf-8')

for res in tweepy.Cursor(api.search, screen_name='@theobserver', q=SEARCH, rpp=100, count=50, result_type="recent", include_entities=True, lang="en").items(num):
    i+=1
    f.write(res.user.screen_name)
    f.write(' ')
    f.write('[')
    f.write((res.created_at.strftime("%d/%b/%Y:%H:%M:%S %Z")).replace(' ', ''))
    f.write(']')	
    f.write(" ")
    f.write('*"')
    f.write(res.text.replace('\n',''))
    f.write('*"')
    f.write(" ")
    f.write(str(res.user.followers_count))
    f.write(" ")
    f.write(str(res.retweet_count))
    f.write('\n')
f.close
print("Tweets retrieved ",i)