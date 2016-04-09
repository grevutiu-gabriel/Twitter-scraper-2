import sys
import twitter
import time
import re
import os

RUN = True
MAX_ID = 693886532965502977 

#TODO: make a pretty print function

print('Twitter hashtag scraper')

#api keys / oauth stuff

if (len(sys.argv) != 6):
  print("invalid number of arguments supplied!")
  sys.exit()

CONSUMER_KEY = sys.argv[1]
CONSUMER_SECRET = sys.argv[2]
ACCESS_TOKEN_KEY = sys.argv[3]
ACCESS_TOKEN_SECRET = sys.argv[4]
SEARCH_STRING = "#" + sys.argv[5]


api = twitter.Api(consumer_key = str(CONSUMER_KEY),
  consumer_secret = str(CONSUMER_SECRET),
  access_token_key = str(ACCESS_TOKEN_KEY),
  access_token_secret = str(ACCESS_TOKEN_SECRET),
  sleep_on_rate_limit=True)

#print(api.VerifyCredentials())

response = api.GetSearch(term=SEARCH_STRING, count=100, until="2015-12-31")

if (len(response) == 0):
  sys.exit("End of tweet index - can't search back any farther")
else:
  last_id = response[len(response) - 1].id - 1
  print("Last id was ", last_id)


print(api.rate_limit.get_limit("http://twitter.com/search/tweets"))

while RUN:
  print("Getting 100 tweets...")
  response = api.GetSearch(term = SEARCH_STRING, count = 100, max_id = last_id)
  if (len(response) == 0):
    sys.exit("End of tweet index - can't search back any farther :v")
  else:
    last_id = response[len(response) - 1].id
    print("Last id was ", last_id, ", Created at: ", response[len(response) - 1].created_at)

  print("remaining requests: ", api.rate_limit.get_limit("http://twitter.com/search/tweets")[1])
