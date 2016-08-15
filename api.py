# import json
# import urllib
# import requests
# import urllib2

from twitter import *

config = {}
execfile("config.py", config)

twitter = Twitter(
            auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

query = twitter.search.tweets(q = "#manypeoplearesaying")

print "Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"])


for result in query["statuses"]:
  # print "(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"])
    print result["text"].encode('utf-8')

# url = "https://api.twitter.com/1.1/search/tweets.json?"
# data = '{"q":[@hannahrcutler]}'

# response = requests.get(url, data=data)
# if (response.ok):
#   jData = json.loads(response.content)
#   for key in jData:
#     print jData[key]
# else:
#   print response.raise_for_status()