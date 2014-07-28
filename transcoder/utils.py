from videogrep.tools.video_downloader import get_single_url
from urllib import urlopen, urlretrieve, urlcleanup
from bs4 import BeautifulSoup

#http://zulko.github.io/blog/2014/07/26/a-tweets-controlled-python-script/

def get_tweets(username):
    url = urlopen("https://twitter.com//" + username)
    page = BeautifulSoup(url)
    url.close()

    tweets = [p.text for p in page.findAll("p")
            if ("class" in p.attrs) and
            ("ProfileTweet-text" in p.attrs["class"])]

    prof_pic = [img.attrs["src"] for img in page.findAll("img")
                if ("class" in img.attrs) and
                ("ProfileAvatar-image" in img.attrs["class"])]
    urlretrieve(prof_pic[0], 'james.jpg')
    urlcleanup()
    return tweets

def pull_url(url):
    return get_single_url(url)
