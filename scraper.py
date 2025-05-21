import requests
from bs4 import BeautifulSoup
import csv
import argparse

from utils import clean_text

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

def scrape_books(max_items):
    books = []
    page = 1
    while len(books) < max_items:
        url = BASE_URL.format(page)
        response = requests.get(url)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.select("article.product_pod")
        if not articles:
            break

        for article in articles:
            title = clean_text(article.h3.a["title"])
            price = clean_text(article.select_one(".price_color").text)
            availability = clean_text(article.select_one(".instock.availability").text)
            books.append({
                "Title": title,
                "Price": price,
                "Availability": availability
            })
            if len(books) >= max_items:
                break
        page += 1

    return books

def save_to_csv(data, filename="products.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Price", "Availability"])
        writer.writeheader()
        for item in data:
            writer.writerow(item)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape product info from a demo bookstore.")
    parser.add_argument("-n", "--number", type=int, default=10, help="Number of products to scrape")
    args = parser.parse_args()

    print(f" Scraping {args.number} products...")
    books = scrape_books(args.number)
    save_to_csv(books)
    print(f" Saved {len(books)} products to products.csv")
