package main

import (
	"fmt"

	"github.com/ChimeraCoder/anaconda"
	"github.com/drhodes/golorem"
	"github.com/fatih/color"
)

type Zwisterer struct {
	api *anaconda.TwitterApi
}

func MakeZwisterer() Zwisterer {
	anaconda.SetConsumerKey(MyConsumerKey())
	anaconda.SetConsumerSecret(MyConsumerSecret())
	api := anaconda.NewTwitterApi(MyToken(), MyTokenSecret())
	return Zwisterer{api}
}

func (z *Zwisterer) Tweet(tweet string) {
	z.api.PostTweet(tweet, nil)
	color.Blue("Zwisterer has tweeted ")
	fmt.Println("  " + tweet)
}

func (z *Zwisterer) TweetRandomLorem() {
	var tweet string
	for i := 0; i <= 14; i++ {
		tweet += lorem.Word(2, 10)
		tweet += " "
	}
	z.Tweet(tweet)
}

func main() {
	zwisterer := MakeZwisterer()
	//zwisterer.Tweet("yes thanks.")
	zwisterer.TweetRandomLorem()
}
