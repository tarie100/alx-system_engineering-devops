#!/usr/bin/python3
""" function that queries the Reddit API and returns the number of subscribers
"""


import requests

def search_results_redirect(query):
    url = f"https://www.reddit.com/search?q={query}"
    headers = {'User-Agent': 'Your Custom User Agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 302 and 'Location' in response.headers:
            return response.headers['Location']
        else:
            return None

    except:
        return None
