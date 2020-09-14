import requests
import json


def test(threshold):
    usernames = []
    itr=1
    resp = requests.get(
        "https://jsonmock.hackerrank.com/api/article_users?page="+str(itr))
    author_info = resp.json()
    # print(json.dumps(author_info, indent=2))
    for author in author_info['data']:
        if "username" in author:
            if author['username']:
                if author['submission_count']>threshold:
                    usernames.append(author['username'])
    while itr<author_info['total_pages']:
        itr+=1
        resp = requests.get(
        "https://jsonmock.hackerrank.com/api/article_users?page="+str(itr))
        author_info = resp.json()
        # articles = resp2.json()
        print(json.dumps(author_info, indent=2))
        for author in author_info['data']:
            if "username" in author:
                if author['username']:
                    if author['submission_count']>threshold:
                        usernames.append(author['username'])
    print(len(set(usernames)), usernames)
    return usernames


test(10)
