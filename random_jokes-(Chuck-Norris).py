import requests

def fetch_joke():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        joke = data["data"]["content"]
        return joke
    else:
        raise Exception("Failed to fetch joke from API")
    
if __name__ == "__main__":
    joke = fetch_joke()
    print(joke)