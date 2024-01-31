import requests

def get_github_data(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repositories = response.json()
        for repo in repositories:
            repo_name = repo["name"]
            repo_language = repo["language"]
            repo_stars = repo["stargazers_count"]
            print(f"Repository:\n {repo_name}\n Language: {repo_language}\n Stars: {repo_stars}\n")
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Заменете "YOUR_USERNAME" с вашето GitHub потребителско име
github_username = input("Input GidHub name: ")

get_github_data(github_username)