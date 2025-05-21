# ProductScraper

A simple Python web scraper that extracts book information (title, price, and availability) from a demo e-commerce website and saves it to a CSV file.

## Features

- Scrapes a user-defined number of products
- Outputs to a clean CSV file
- Built with `requests` and `BeautifulSoup`
- CLI-friendly with arguments

## Usage

```bash
pip install -r requirements.txt
python scraper.py -n 20
```

This will scrape 20 products and save them to `products.csv`.

## Example Output

| Title                         | Price  | Availability |
|------------------------------|--------|---------------|
| The Grand Design             | £13.76 | In stock      |
| Tipping the Velvet           | £53.74 | In stock      |
