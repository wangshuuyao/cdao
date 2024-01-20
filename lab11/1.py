from github import Github


token = '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'

g = Github(token)

user = g.get_user()

following = user.get_following()

for follower in following:
    print(f"Follower: {follower.login}")

    repos = follower.get_repos()

    for repo in repos:
        print(f"  Repo: {repo.name}")

        with open('follower_repos.txt', 'a') as file:
            file.write(f"{follower.login}/{repo.name}\n")