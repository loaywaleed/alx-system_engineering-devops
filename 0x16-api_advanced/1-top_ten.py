#!/usr/bin/python3
"""Top ten hot posts for a given subreddit"""


def top_ten(subreddit):
    """Gets top ten hot posts in a subreddit"""
    import requests

    user_agent = {"User-Agent": "anon"}

    api_response = requests.get(
        "https://www.reddit.com//r/{}/hot.json?limit=10".format(subreddit),
        headers=user_agent, allow_redirects=False)

    if api_response.status_code == 200:
        for item in api_response.json().get("data").get("children"):
            print(item.get("data").get("title"))

    else:
        print("None")
