import requests


NINJAS_KEY = "vk47EpqwD07BnO+nL8O4Gg==CoPeTzJTrksmlvHq"


# get the quotes from ninjas api
def morning():
    category = "morning"
    api_url = "https://api.api-ninjas.com/v1/quotes?category={}&limit=1".format(
        category
    )
    response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY})
    if response.status_code == requests.codes.ok:
        quotes = response.json()
        quote = quotes[0]["quote"]
        author = quotes[0]["author"]
        return quote, author
    else:
        return ("Error:", response.status_code, response.text)


def dad_joke():
    api_url = "https://api.api-ninjas.com/v1/dadjokes?limit={}".format(1)
    response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY})
    if response.status_code == requests.codes.ok:
        dad_jokes = response.json()
        joke = dad_jokes[0]["joke"]
        return joke
    else:
        return ("Error:", response.status_code, response.text)


def fact():
    api_url = "https://api.api-ninjas.com/v1/facts?limit={}".format(1)
    response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY})
    if response.status_code == requests.codes.ok:
        facts = response.json()
        fact = facts[0]["fact"]
        return fact
    else:
        return ("Error:", response.status_code, response.text)
