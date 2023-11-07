#!/usr/bin/python3
"""A script that gets subscriber count of a subreddit"""


def number_of_subscribers(subreddit):
    import requests
    user_agent = {"User-Agent": "anon"}
    api_response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers=user_agent, allow_redirects=False)

    if api_response.status_code == 200:
        return api_response.json().get("data").get("subscribers")

    return 0
