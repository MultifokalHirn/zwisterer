import wikipedia
from templateBot import TemplateBot
import code
import random


class Fotzebot(TemplateBot):

    def __init__(self, name, catchphrase):
        self.setAttributes(name, catchphrase)
        self.setWords()
        self.login()

    def tweetAFotze(self):
        fotze = self.getFotze()
        self.tweetAndPrint(fotze)

    def getFotze(self):
        rndtopic = self.getTopic()
        rndtopic = rndtopic.replace(u"-", u"")
        unwantedchars = u"!@#$()"
        for char in unwantedchars:
            rndtopic = rndtopic.replace(char, u"-")
        rndtopic = rndtopic.replace(u" ", u"-")
        fotze = rndtopic + u"-" + random.choice(self.words)
        fotze = fotze.replace(u"--", u"-")
        return fotze.encode('utf-8')

    def getTopic(self):
        art = wikipedia.page(title=wikipedia.random(pages=1))
        code.interact(local=locals())
        print art.categories
        return art.title()

    def setWords(self):
        self.words = [u'Fotze', u'Spacko', u'Nase', u'Macker', u'Wurst', u'Wutz', u'Flaxe', u'Nazi', u'Ficker', u'Bitch', u'Max', u'Terrorist', u'Scheisser', u'Borste', u'Arsch', u'Porno']

# keys for @kosename
    def myConsumerkey(self):
        return "qR0SNpmgr1EbfQp3g2weo5pjm"

    def myConsumerSecret(self):
        return "GlrYqW2Hd1bPGe4bore8LEpeDf9nrdKWhxqkELbHpBpWT4SXAV"

    def myToken(self):
        return "757293607439233024-5VplCP70bdp4iIKwl0JDJQkPkJLcSMT"

    def myTokenSecret(self):
        return "eWuiTDpe6gAJ4TkK6hq4gJVSsKfqgDCHNkXelVWhN6VW3"

i = Fotzebot("Fotzebot", "Fotzebot.")
i.introduceYourself()
wikipedia.set_lang("de")
# i.tweet("FOTZE!".upper())
# code.interact(local=locals())
while(True):
    print i.getFotze()
    # i.tweetAFotze()
    i.sleepForXseconds(2)
