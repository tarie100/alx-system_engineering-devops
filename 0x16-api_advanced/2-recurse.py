#!/usr/bin/python3
"""
  Recursively fetches the titles of the hot posts from a subreddit.
"""
import requests


def recurse(subreddit, hot_list=None):
    if hot_list is None:
        hot_list = []
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Your Custom User Agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json()
        
        if response.status_code == 200 and 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            
            for post in posts:
                hot_list.append(post['data']['title'])
                
            if 'after' in data['data'] and data['data']['after'] is not None:
                after = data['data']['after']
                return recurse(subreddit, hot_list=hot_list, after=after)
            
            return hot_list
            
        else:
            return None
        
    except:
        return None
