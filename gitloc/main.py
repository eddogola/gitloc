from typing import List
import os

import github
from github import Github, Auth


def get_g(access_token: str) -> github.MainClass.Github:
    auth = Auth.Token(access_token)

    return Github(auth=auth)


def get_repos(g: github.MainClass.Github) -> List:
    return list(g.get_user().get_repos())


def get_file_contents(repo: github.Repository.Repository, file: dict) -> str:
    content = repo.get_contents(file["path"])
    # unpack tree/directory

    return content


if __name__ == "__main__":
    g = get_g(os.getenv("ACCESS_TOKEN"))
    repos = get_repos(g)
    repo = repos[0]
    try:
        branch_name = "main"
        latest_commit = repo.get_commit(sha=branch_name)
    except github.GithubException:
        branch_name = "master"
        latest_commit = repo.get_commit(sha=branch_name)
    tree_hash = latest_commit.commit.tree.sha
    tree = repo.get_git_tree(sha=tree_hash, recursive=True)

    # each is a dict with fields: path, mode, type, sha, url
    files = tree.raw_data["tree"]
    file = files[0]
    print(get_file_contents(repo, file))
