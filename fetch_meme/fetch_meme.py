
import os
import requests
from PIL import Image
from io import BytesIO
import subprocess

# Fetch a random coding meme
def fetch_meme():
    url = "https://meme-api.com/memes/programming"  # Example API for memes
    response = requests.get(url)
    if response.status_code == 200:
        memes = response.json().get("memes", [])
        if memes:
            meme = memes[0]
            image_url = meme.get("url")
            if image_url:
                return image_url
    return None

# Save the meme locally
def save_meme(image_url, save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image.save(save_path)
        return save_path
    return None

# Display meme in the terminal
def display_meme(image_path):
    subprocess.run(["chafa", image_path])  # Requires `chafa` to be installed

if __name__ == "__main__":
    meme_url = fetch_meme()
    if meme_url:
        meme_path = os.path.join(os.path.dirname(__file__), "../memes/meme.jpg")
        os.makedirs(os.path.dirname(meme_path), exist_ok=True)
        saved_path = save_meme(meme_url, meme_path)
        if saved_path:
            display_meme(saved_path)
    else:
        print("Failed to fetch a meme. Try again later!")
