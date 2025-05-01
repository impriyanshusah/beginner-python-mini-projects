import requests
from PIL import Image
from io import BytesIO

url = "https://api.freeapi.app/api/v1/public/cats/cat/random"

def fetch_cat_details(url):
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        catName = data["data"]["name"]
        catOrigin = data["data"]["origin"]
        catDescription = data["data"]["description"]
        catImageUrl = data["data"]["image"]
        return catName, catOrigin, catDescription, catImageUrl
    else:
        raise Exception("Failed to fetch cat data from API")

    
def main():
    try:
        catName, catOrigin, catDescription,catImageUrl = fetch_cat_details(url)
        print(f"Name: {catName}")
        print(f"Origin: {catOrigin}")
        print(f"Description: {catDescription}")
        response = requests.get(catImageUrl)
        img = Image.open(BytesIO(response.content))
        img.show()
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
