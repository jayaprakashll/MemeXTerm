import os
import requests
from PIL import Image
from io import BytesIO
import subprocess
import random
import argparse

# Fetch a random coding meme
def fetch_meme(category="programming"):
    url = f"https://meme-api.com/memes/{category}"  # Example API for memes
    try:
        response = requests.get(url)
        if response.status_code == 200:
            memes = response.json().get("memes", [])
            if memes:
                meme = random.choice(memes)
                image_url = meme.get("url")
                return image_url
    except Exception as e:
        print(f"Error fetching meme: {e}")
    return None

# Save the meme locally
def save_meme(image_url, save_path):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            image.save(save_path)
            return save_path
    except Exception as e:
        print(f"Error saving meme: {e}")
    return None

# Display meme in the terminal
def display_meme(image_path):
    try:
        subprocess.run(["chafa", image_path])  # Requires `chafa` to be installed
    except FileNotFoundError:
        print("Error: `chafa` is not installed. Please install it to display memes in the terminal.")

# Get random meme from cache
def get_random_cached_meme(cache_dir):
    try:
        cached_memes = [os.path.join(cache_dir, f) for f in os.listdir(cache_dir) if f.endswith(".jpg")]
        if cached_memes:
            return random.choice(cached_memes)
    except Exception as e:
        print(f"Error accessing cache: {e}")
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch and display coding memes in your terminal.")
    parser.add_argument("--category", type=str, default="programming", help="Specify meme category (default: programming)")
    parser.add_argument("--use-cache", action="store_true", help="Use cached memes if available")
    args = parser.parse_args()

    cache_dir = os.path.join(os.path.dirname(__file__), "../memes")
    os.makedirs(cache_dir, exist_ok=True)

    meme_url = None
    if args.use_cache:
        meme_path = get_random_cached_meme(cache_dir)
    else:
        meme_url = fetch_meme(args.category)
        if meme_url:
            meme_path = os.path.join(cache_dir, f"meme_{random.randint(1000, 9999)}.jpg")
            meme_path = save_meme(meme_url, meme_path)

    if meme_path and os.path.exists(meme_path):
        display_meme(meme_path)
    else:
        print("Failed to fetch or display a meme. Try again later!")
