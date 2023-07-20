from typing import List
import os

import github
from github import Github, Auth


def get_g(access_token: str) -> github.MainClass.Github:
    auth = Auth.Token(access_token)

    return Github(auth=auth)


def get_repos(g: github.MainClass.Github) -> List:
    return list(g.get_user().get_repos())


if __name__ == "__main__":
    g = get_g(os.getenv("ACCESS_TOKEN"))
    print(get_repos(g))
    # print(get_repos(g))
