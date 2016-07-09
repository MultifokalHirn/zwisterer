import wikipedia
import tweepy
import random
import time

class Zwisterer:

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
        try:
            page = wikipedia.page(aTopic).content
        except:
            self.thinkAbout(aTopic)
            return
        print self.name + " is thinking about " + aTopic + "."
        sentences = page.split(". ")
        tweet = sentences[random.randint(0, len(sentences)-1)] + "."
        while self.isOverXChars(tweet, 140):
            tweet = sentences[random.randint(0, len(sentences)-1)] + "."
        return tweet

    def thinkAboutSomethingRandom(self):
        topic = wikipedia.random(pages=1)
        return self.thinkAbout(topic)

    def thinkAboutSomethingRandomThatContains(self, thought, int):
        print int
        topic = wikipedia.random(pages=1)
        try:
            content = wikipedia.page(topic).content
        except:
            self.thinkAboutSomethingRandomThatContains(thought, (int+1))
            return
        if thought in content:
            sentences = content.split(". ")
            for sentence in sentences:
                if not self.isOverXChars(sentence, 140):
                    if thought in sentence:
                        self.tweet(sentence)
                        return
        self.thinkAboutSomethingRandomThatContains(thought, (int+1))

    def isOverXChars(self, tweet, x):
        return (len(tweet) > x)

    def isTitle(self, tweet):
        if "==" in tweet:
            return True
        return False

    def isMeaningless(self, tweet):
        if (("==" in tweet) | ("ISBN" in tweet) | ("*" in tweet)):
            return True
        return False

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

    def tweetToUserAboutSomethingRandom(self, user):
        tweet = self.thinkAboutSomethingRandom()
        if not self.tweetToUser(user, tweet):
            self.tweetToUserAboutSomethingRandom(user)
        return

    def tweetToUser(self, user, tweet):
        maxTweetlength = 137 - len(user.screen_name)
        if (self.isOverXChars(tweet, maxTweetlength) | self.isMeaningless(tweet)):
            return False
        newTweet = "@" + user.screen_name + ": " + tweet
        self.tweet(newTweet)
        return True

    def showFollowers(self):
        for follower in self.followers:
            print follower.screen_name

    def introduceYourself(self):
        print "Hi! I am " + self.name + ", your new zwisterer!"
        print "I will now do my thing."
        print "To stop me from doing so just press ctrl-d"
        print " "

    def myConsumerkey(self):
        return "2BVnyuOwELvw6tHYhEUFDCphF"

    def myConsumerSecret(self):
        return "SN9buLAxcJmm3tPGqCYqAGZS2XpC6QH6EkZjomap1FbQVWoHj9"

    def myToken(self):
        return "722838560928174082-M4UJBgUuSscZtnrTE8JdT9YtcTEQOCA"

    def myTokenSecret(self):
        return "fraffLzrJActUqVHBXGST8GxYtZesjpC25Db85PYcY7dC"


z = Zwisterer("Zwakke")
z.introduceYourself()
# wikipedia.set_lang("en")
wikipedia.set_lang("en")
# wikipedia.set_lang("fr")

while(True):
    # follower = z.followers[random.randint(0, len(z.followers)-1)]
    # z.tweetToUserAboutSomethingRandom(follower)
    z.tweetAboutSomethingRandom()
    print " "
    time.sleep(5)
