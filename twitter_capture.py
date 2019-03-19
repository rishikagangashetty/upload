import tweepy
import time

ACCESS_TOKEN = '1107629035117596672-kHjrpTe6slTDzub0YgxqmktJuyzA1S'
ACCESS_SECRET = 'sLE2lEBPEzmr7Xyx8aLHqerVT9uYHPSgKVSv91HSBUZll'
CONSUMER_KEY = 'HploXoH1P2bKZdR3MHmxKzGK0'
CONSUMER_SECRET = 'fhhHr6zs2YthPLQhmstRoTLgvsUhU62rY3Sjirwsq3ToxSY21e'
SEARCH=input("Enter search string ")
#FROM=input("Enter from date (YYYY-MM-DD format) ")
#TO=input("Enter the to data (YYYY-MM-DD format) ")
INPUT_FILE_PATH= './'+SEARCH+'.txt'

number_ssdi=int(input("Enter the number of tweets you want to retrieve: "))
authorisation = tweepy.authorisation.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
authorisation.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api_rish = tweepy.API(authorisation)
a=0;

r = open(INPUT_FILE_PATH, 'w', encoding='utf-8')

for res in tweepy.Cursor(api_rish.search, q=SEARCH).items(number_ssdi):
	a=a+1
	r.write(res.user.screen_name)
	r.write(' ')
	r.write('[')
	r.write(res.created_at.strftime("%d/%b/%Y:%H:%M:%S %Z"))
	r.write(']')	
	r.write(" ")
	r.write('"')
	r.write(res.text.replace('\n',''))
	r.write('"')
	r.write(" ")
	r.write(str(res.user.followers_count))
	r.write(" ")
	r.write(str(res.retweet_count))
	f.write('\n')
r.close
print("The number of tweets retrieved are",a)