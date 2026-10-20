import json
import requests

URL = "https://dummyjson.com/products?limit=0"
response = requests.get(URL, timeout=30)
response.raise_for_status()
products = response.json()["products"]
with open("products.json", "w") as f:
    json.dump(products, f, indent=2)
    print(f"Saved {len(products)} products to products.json")