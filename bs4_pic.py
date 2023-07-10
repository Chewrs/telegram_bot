from bs4 import BeautifulSoup
import requests
import random


def scrape_image_urls(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the <img> tags in the HTML
    img_tags = soup.find_all("img")

    # Extract the image URLs
    image_urls = []
    for img in img_tags:
        if "data-src" in img.attrs:
            img_url = img["data-src"]
        else:
            img_url = img["src"]

        # Handle relative image URLs
        if not img_url.startswith("http"):
            img_url = requests.compat.urljoin(url, img_url)

        image_urls.append(img_url)

    return image_urls


def get_pic():
    # Example usage
    image_urls = scrape_image_urls("https://sexygirlspics.com/beautiful/")
    pics = []
    # Print the extracted image URLs
    for url in image_urls:
        pics.append(url)

    pic = random.choice(pics)
    return pic


print(get_pic())
