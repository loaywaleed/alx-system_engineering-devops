#!/usr/bin/python3
"""gets all hot posts for a given subreddit"""


def recurse(subreddit, hot_list=[], after=None):
    """Gets all hot posts in a subreddit using recursion"""
    import requests

    user_agent = {"User-Agent": "anon"}

    api_response = requests.get(
        "https://www.reddit.com//r/{}/hot.json".format(
            subreddit),
        params={"after": after},
        headers=user_agent, allow_redirects=False)

    if api_response.status_code == 200:
        [hot_list.append(items.get("data").get("title"))
         for items in api_response.json().get("data").get("children")]
        after = api_response.json().get("data").get("after")
        if not after:
            return hot_list

        return recurse(subreddit, hot_list, after)

    else:
        return None
