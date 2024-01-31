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
            print(f"Repository: {repo_name}, Language: {repo_language}, Stars: {repo_stars}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Заменете "YOUR_USERNAME" с вашето GitHub потребителско име
github_username = input("Input GidHub name: ")

get_github_data(github_username)