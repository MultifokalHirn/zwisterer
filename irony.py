from templateBot import TemplateBot
import code
import random

class IroningMan(TemplateBot):

    def __init__(self, name, catchphrase):
        self.setAttributes(name, catchphrase)
        self.login()
        self.setMyTweets()

    def tweet(self, tweet):
        self.myTweets.append(self.api.update_status(tweet))
        print u'\u2709'

    def getIronicTweet(self):
        tweets = self.getTextOnlyTweetsWith("#irony")
        print len(tweets)
        for tweet in tweets:
            if (len(tweet.text) + len(tweet.user.screen_name) > 137):
                continue
            if self.alreadyTweeted(tweet):
                print tweet.text
                continue
        return self.getIronicTweet()

    def tweetSomeIroning(self):
        tweet = i.getIronicTweet()
        while(True):
            try:
                self.tweet("@" + tweet.user.screen_name + ": " + tweet.text.upper())
                break
            except:
                print "I couldnt tweet " + tweet.text + ". So lets try another one."
                tweet = i.getIronicTweet()
                continue

    def tweetSomeIroningWithPrompt(self):
        tweet = i.getIronicTweet()
        while(True):
            try:
                return self.tweetWithPrompt("@" + tweet.user.screen_name + ": " + tweet.text.upper())
            except:
                print "I couldnt tweet " + tweet.text + ". So lets try another one."
                tweet = i.getIronicTweet()
                continue

i = IroningMan("IRONINGMAN", "Let me do the ironing luv.")
i.introduceYourself()
# i.tweet("Now let me do the ironing luv!".upper())
# code.interact(local=locals())

while(True):
    print ""
    if not i.tweetSomeIroningWithPrompt():
        continue
    i.sleepForXseconds(5)
