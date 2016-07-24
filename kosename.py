from templateBot import TemplateBot
import code
import random

class Kosename(TemplateBot):

    def __init__(self, name, catchphrase):
        self.setAttributes(name, catchphrase)
        self.login()
        self.setMyTweets()

    def tweet(self, tweet):
        self.myTweets.append(self.api.update_status(tweet))

# keys for @kosename
    def myConsumerkey(self):
        return "qR0SNpmgr1EbfQp3g2weo5pjm"

    def myConsumerSecret(self):
        return "GlrYqW2Hd1bPGe4bore8LEpeDf9nrdKWhxqkELbHpBpWT4SXAV"

    def myToken(self):
        return "757293607439233024-5VplCP70bdp4iIKwl0JDJQkPkJLcSMT"

    def myTokenSecret(self):
        return "eWuiTDpe6gAJ4TkK6hq4gJVSsKfqgDCHNkXelVWhN6VW3"


i = Kosename("Kosename", "I am looking into some Kosenamens.")
i.introduceYourself()
i.tweet("test")
# code.interact(local=locals())

# while(True):
#     print ""
#     if not i.tweetSomeIroningWithPrompt():
#         continue
#     i.sleepForXseconds(5)
