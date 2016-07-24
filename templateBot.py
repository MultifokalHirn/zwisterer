import tweepy
import random
import time
import code

class TemplateBot:

    def __init__(self, name, catchphrase):
        self.setAttributes(name, catchphrase)
        self.login()
        # self.setFollowers()

    def setAttributes(self, name, catchphrase):
        self.name = name
        self.catchphrase = catchphrase
        self.yes = set(['yes', 'y', 'ye', ''])
        self.no = set(['no', 'n'])
        self.tweetCache = {}

    def login(self):
        self.auth = tweepy.OAuthHandler(
            self.myConsumerkey(), self.myConsumerSecret())
        self.auth.set_access_token(self.myToken(), self.myTokenSecret())
        self.api = tweepy.API(self.auth)

    def tweet(self, tweet):
        self.api.update_status(tweet)
        # print u'\u2709'

    def tweetAndPrint(self, tweet):
        self.tweet(tweet)
        print self.name + " has twittered: " + tweet

    def tweetWithPrompt(self, tweet):
        print "I want to tweet this:"
        print tweet
        print "is that okidoki?"
        choice = raw_input().lower()
        if choice in self.yes:
            self.tweet(tweet)
            return True
        elif choice in self.no:
            print "k. thought so."
            return False
        else:
            print "wut? i bet u meant yes or something, so i go tweet it"
            self.tweet(tweet)
            return True

    def tweetToUser(self, user, tweet):
        maxTweetlength = 137 - len(user.screen_name)
        if (self.isOverXChars(tweet, maxTweetlength) | self.isMeaningless(tweet)):
            return False
        newTweet = "@" + user.screen_name + ": " + tweet
        self.tweet(newTweet)
        return True

    def getMyTweets(self):
        return self.api.user_timeline(count=100)

    def setMyTweets(self):
        self.myTweets = self.searchResultsToList(self.getMyTweets())

    def showMyTweets(self):
        tweets = self.getMyTweets()
        for tweet in tweets:
            print tweet.text + "\n"

    def getMyLatestTweet(self):
        return self.api.user_timeline(count=1)

    def showMyLatestTweet(self):
        print self.getMyLatestTweet().text

    def alreadyTweeted(self, tweet):
        # needs myTweets to be set
        for oldTweet in self.myTweets:
            if tweet.text.lower() in oldTweet.text.lower():
                return True
        return False

    def getFollowers(self):
        followers = []
        ids = self.api.followers_ids()
        for follower_id in ids:
            followers.append(self.api.get_user(follower_id))
        return followers

    def setFollowers(self):
        self.followers = self.getFollowers()

    def showFollowers(self):
        for follower in self.followers:
            print follower.screen_name

    def introduceYourself(self):
        print "Hi! I am " + self.name + ", your new bot!"
        print self.catchphrase
        print "To stop me from doing so just press ctrl-d"

    def getTweetsWith(self, query):
        if query not in self.tweetCache:
            self.tweetCache[query] = [self.searchResultsToList(self.api.search(q=query, count=100)), 0]
        else:
            pageno = self.tweetCache[query][1] + 1
            print "pageno ", pageno
            maxid = self.idOfOldestTweet(self.tweetCache[query][0])
            self.tweetCache[query] = [self.searchResultsToList(self.api.search(q=query, count=100, max_id=maxid, page=pageno)), pageno]
        return self.tweetCache[query][0]

    def getTextOnlyTweetsWith(self, query):
        l = []
        for tweet in self.getTweetsWith(query):
            if "@" in tweet.text:
                continue
            elif "http" in tweet.text:
                continue
            else:
                l.append(tweet)
        return l

    def getRandomTweetWith(self, query):
        tweets = self.getTweetsWith(query)
        return tweets.pop(random.randint(0, len(tweets)-1))

# refactor the ifs, magnifying glass icon
    def getTextOnlyTweetWith(self, query):
        # print u'\uE114' + " looking for " + query + "..."
        tweets = random.shuffle(self.getTweetsWith(query))
        h = True
        while(h):
            tweet = tweets.pop()
            if len(tweets) < 1:
                return tweet
            if "@" in tweet.text:
                continue
            elif "http" in tweet.text:
                continue
            else:
                return tweet

    def getTextOnlyTweetOlderThanWith(self, maxid, query):
        # print u'\uE114' + " looking for " + query + "..."
        tweets = random.shuffle(self.api.search(q=query, count=100, max_id=maxid))
        h = True
        while(h):
            tweet = tweets.pop()
            if len(tweets) < 1:
                return tweet
            if "@" in tweet.text:
                continue
            elif "http" in tweet.text:
                continue
            else:
                return tweet

    def sleepForXseconds(self, x):
        for i in range(x):
            time.sleep(1)
        else:
            print

    def searchResultsToList(self, results):
        l = []
        for tweet in results:
            l.append(tweet)
        return l

    def idOfOldestTweet(self, list):
        # code.interact(local=locals())
        return list[-1].id


# keys for @zwisterer
    def myConsumerkey(self):
        return "2BVnyuOwELvw6tHYhEUFDCphF"

    def myConsumerSecret(self):
        return "SN9buLAxcJmm3tPGqCYqAGZS2XpC6QH6EkZjomap1FbQVWoHj9"

    def myToken(self):
        return "722838560928174082-M4UJBgUuSscZtnrTE8JdT9YtcTEQOCA"

    def myTokenSecret(self):
        return "fraffLzrJActUqVHBXGST8GxYtZesjpC25Db85PYcY7dC"


# bot = TemplateBot("bot", "i cant do anything on my own...")
# bot.introduceYourself()
#
# print "\nYou have launched a templatebot with no intrinsic behavior. "
# print "We will open a REPL for you to interact with it. Close it with ctrl-z."
# print "Usage example: bot.tweet('hello world')\n"
#
# code.interact(local=locals())

# the loop should look something like
# while(True):
#     print ""
#         bot.tweet("hii")
#         continue
#     # wait 5 sec
#     time.sleep(5)
