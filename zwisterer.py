import wikipedia
import tweepy
import random

class Zwisterer:
    'a zwisterer'

    def __init__(self, name):
        self.auth = tweepy.OAuthHandler(
            self.myConsumerkey(), self.myConsumerSecret())
        self.auth.set_access_token(self.myToken(), self.myTokenSecret())
        self.api = tweepy.API(self.auth)
        self.name = name
        self.followers = self.getFollowers()

    def tweet(self, aTweet):
        self.api.update_status(aTweet)
        print self.name + " has twittered: " + aTweet

    def myTimeline(self):
        public_tweets = self.api.home_timeline()
        for tweet in public_tweets:
            print tweet.text

    def tweetAbout(self, aTopic):
        tweet = self.thinkAbout(aTopic)
        self.tweet(tweet)

    def tweetAboutSomethingRandom(self):
        tweet = self.thinkAboutSomethingRandom()
        self.tweet(tweet)

    def thinkAbout(self, aTopic):
        page = wikipedia.page(aTopic).content
        sentences = page.split(". ")
        tweet = sentences[random.randint(0, len(sentences)-1)] + "."
        while self.isOverXChars(tweet, 140):
            tweet = sentences[random.randint(0, len(sentences)-1)] + "."
        return tweet

    def thinkAboutSomethingRandom(self):
        topic = wikipedia.random(pages=1)
        return self.thinkAbout(topic)

    def thinkAboutSomethingRandomThanContains(self, thought, int):
        print int
        topic = wikipedia.random(pages=1)
        try:
            content = wikipedia.page(topic).content
        except:
            self.thinkAboutSomethingRandomThanContains(thought, (int+1))
            return
        if thought in content:
            sentences = content.split(". ")
            for sentence in sentences:
                if not self.isOverXChars(sentence, 140):
                    if thought in sentence:
                        self.tweet(sentence)
                        return
        self.thinkAboutSomethingRandomThanContains(thought, (int+1))

    def isOverXChars(self, tweet, x):
        return (len(tweet) > x)

    def getFollowers(self):
        followers = []
        ids = self.api.followers_ids()
        for follower_id in ids:
            followers.append(self.api.get_user(follower_id))
        return followers

    def tweetToUserAbout(self, user, topic):
        tweet = self.thinkAbout(topic)
        if not self.tweetToUser(user, tweet):
            self.tweetToUserAbout(user, topic)
        return

    def tweetToUser(self, user, tweet):
        maxTweetlength = 137 - len(user.screen_name)
        if self.isOverXChars(tweet, maxTweetlength):
            return False
        newTweet = "@" + user.screen_name + ": " + tweet
        self.tweet(newTweet)
        return True

    def showFollowers(self):
        for follower in self.followers:
            print follower.screen_name

    def myConsumerkey(self):
        return "2BVnyuOwELvw6tHYhEUFDCphF"

    def myConsumerSecret(self):
        return "SN9buLAxcJmm3tPGqCYqAGZS2XpC6QH6EkZjomap1FbQVWoHj9"

    def myToken(self):
        return "722838560928174082-M4UJBgUuSscZtnrTE8JdT9YtcTEQOCA"

    def myTokenSecret(self):
        return "fraffLzrJActUqVHBXGST8GxYtZesjpC25Db85PYcY7dC"


z = Zwisterer("zwisterer")
# wikipedia.set_lang("en")
# z.thinkAboutSomethingRandom()
wikipedia.set_lang("de")
# z.thinkAboutSomethingRandom()
# wikipedia.set_lang("fr")
# # z.thinkAboutSomethingRandom()
# z.thinkAboutSomethingRandomThanContains("thanks", 0)
user = z.followers[0]
z.tweetToUserAbout(user, "Friedrich Nietzsche")

# z.tweet(tweet)
