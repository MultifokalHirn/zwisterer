import wikipedia
import tweepy

class Zwisterer:
    'a zwisterer'

    def __init__(self, name):
        self.auth = tweepy.OAuthHandler(
            self.myConsumerkey(), self.myConsumerSecret())
        self.auth.set_access_token(self.myToken(), self.myTokenSecret())
        self.api = tweepy.API(self.auth)
        self.name = name

    def tweet(self, aTweet):
        self.api.update_status(aTweet)

    def myTimeline(self):
        public_tweets = self.api.home_timeline()
        for tweet in public_tweets:
            print tweet.text

    def myConsumerkey(self):
        return "2BVnyuOwELvw6tHYhEUFDCphF"

    def myConsumerSecret(self):
        return "SN9buLAxcJmm3tPGqCYqAGZS2XpC6QH6EkZjomap1FbQVWoHj9"

    def myToken(self):
        return "722838560928174082-M4UJBgUuSscZtnrTE8JdT9YtcTEQOCA"

    def myTokenSecret(self):
        return "fraffLzrJActUqVHBXGST8GxYtZesjpC25Db85PYcY7dC"


z = Zwisterer("zwisterer")
tweet = "i am now pythonbot, not golangbot :'('"
z.tweet(tweet)
