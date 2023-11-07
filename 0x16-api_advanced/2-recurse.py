#!/usr/bin/python3
""" Task2 """
import requests


def recurse(subreddit, hot_list=[], count=0, after=''):
    """Queries the Reddit API and returns all hot posts of the subreddit"""
    base = 'https://www.reddit.com/'
    endpoint = 'r/{}/hot.json'.format(subreddit)
    query_string = '?show="all"&limit=100&after={}&count={}'.format(
        after, count)
    url = base + endpoint + query_string
    headers = {'User-Agent': 'My-User-Agent'}
    response = requests.get(url, headers=headers)
    if not response.ok:
        if len(hot_list) == 0:
            return None
        else:
            return hot_list

    data = response.json()['data']
    for post in data['children']:
        hot_list.append(post['data']['title'])
    after = data['after']
    dist = data['dist']
    if (after):
        recurse(subreddit, hot_list, count + dist, after)

    if len(hot_list) == 0:
        return None
    else:
        return hot_list
