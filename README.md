# Twitter-scraper
python script to scrape the (available) tweet index for a specified hashtag

I was writing this for a class I'm in (we were wanted to go scrape 3-5 years of tweets from twitter, similar to what [scraperwiki](https://scraperwiki.com) used to do before it cost money).

However, it turns out that the only api-exposed method of grabbing hashtag data is via the [search method in their api](https://dev.twitter.com/rest/reference/get/search/tweets), which only contains the past ~9 days of data, roughly. 

If you want to grab all the incoming tweets, then you can do so via the streaming API.

I can't do what I originally set out to do with this (get ~3 years of tweets) and that'll require a web scraper, so I'm just posting this up since it's still useful for grabbing all the tweets on the search api.
