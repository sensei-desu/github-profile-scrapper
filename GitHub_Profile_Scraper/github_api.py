import requests

GITHUB_API = "https://api.github.com"


def get_headers():
    return {
        "Accept": "application/vnd.github+json",
        "User-Agent": "GitHub-Profile-Scraper"
    }


def get_github_profile(username):
    url = f"{GITHUB_API}/users/{username}"
    response = requests.get(url, headers=get_headers(), timeout=10)

    if response.status_code == 404:
        return None

    response.raise_for_status()
    data = response.json()

    return {
        "username": data.get("login"),
        "name": data.get("name"),
        "bio": data.get("bio"),
        "avatar": data.get("avatar_url"),
        "location": data.get("location"),
        "followers": data.get("followers", 0),
        "following": data.get("following", 0),
        "repositories": data.get("public_repos", 0),
        "created": data.get("created_at"),
        "profile_url": data.get("html_url")
    }


def get_repositories(username):
    url = f"{GITHUB_API}/users/{username}/repos"
    params = {
        "sort": "updated",
        "per_page": 6
    }

    response = requests.get(
        url,
        params=params,
        headers=get_headers(),
        timeout=10
    )

    if response.status_code != 200:
        return []

    repositories = []

    for repo in response.json():
        repositories.append({
            "name": repo.get("name"),
            "description": repo.get("description"),
            "language": repo.get("language"),
            "stars": repo.get("stargazers_count", 0),
            "url": repo.get("html_url")
        })

    return repositories
