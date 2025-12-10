import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f'http://api.github.com/users/{username}')
        body = r.json()

        return body
    
    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body
    

    #Individual task

    def get_emoji_url(self, emoji_name):
        r = requests.get('https://api.github.com/emojis')
        emojis = r.json()

        return emojis.get(emoji_name)
    

    def get_commit(self, owner, repo, ref, message):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits/{ref}/{message}')
        body = r.json()

        return body
    

    def get_all_user_repos(self, owner):
        r = requests.get(f"https://api.github.com/users/{owner}/repos")
        body = r.json()

        return body

            
