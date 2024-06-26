#!/usr/bin/python3
""" Write a function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit."""
import json
import requests


def top_ten(subreddit):
    """ printtop 10 hot post for a subreddit """
    # the URL for the Reddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # custom User-Agent header to avoid rate limiting
    headers = {'User-Agent': 'MyRedditClient/1.0'}

    # GET request to the Reddit API
    try:
        response = requests.get(url, headers=headers)

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            # Parsed the JSON data from the response
            data = response.json()
            if not response.is_json or not responce.get_json():
                print("None")
                return

            # Check if the subreddit exists
            if 'error' in data:
                print("None")
                return

            # Retrieve and print the titles of the first 10 posts
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print("None")
    except (requests.RequestException, KeyError, json.JSONDecodeError):
        print("None")
        return
