from bs4 import BeautifulSoup
import requests
class AnimePahe():
    def __init__(self) -> None:
        pass

    def search(query):
        json = None
        response = requests.get(f'https://pahe.vercel.app//animepahe/search/{query}', timeout=300)
        if response.status_code == 200:
            json = response.json()

        if not json:
            return
        results = json['results']
        return results

    def get_latest():
        response = requests.get('https://pahe.vercel.app//animepahe/airing', timeout=300).json()
        data = response['data']
        return data

    def get_episode_links(episode_id):
        json = None
        url = "https://pahe.vercel.app//animepahe/download/" + episode_id
        response = requests.get(url, timeout=300)
        if response.status_code == 200:
            json = response.json()
        if not json:
            return        
        return json
    
    
