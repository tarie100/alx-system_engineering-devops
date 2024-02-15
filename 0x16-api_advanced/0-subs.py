#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""


import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/search?q={query}"
    headers = {'User-Agent': 'Your Custom User Agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
