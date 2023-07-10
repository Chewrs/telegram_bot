import requests


def get_meme():
    url = "https://meme-api.com/gimme"
    meme_get = requests.get(url)
    meme_json = meme_get.json()
    meme_pic = meme_json["preview"][-2]

    return meme_pic
