#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
import praw
import requests
import re
import pyquery
import urllib

reddit = praw.Reddit('bot', user_agent="League of Legends Bot by u/redwallguy")

subreddit = reddit.subreddit("leagueoflegends")

i=0
for submission in subreddit.hot(limit=10):
    if i==0:
        print(dir(submission))
    else:
        if not submission.is_self:
            print(submission.url)
    i+=1
