import json
from database import Base, SessionLocal, engine
from models import Category, Product

# Recreate the tables so the script can be re-run safely
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


with open("products.json") as f:
    items = json.load(f)


db = SessionLocal()


# One Category row per unique category name
categories = {}
for name in {item["category"] for item in items}:
    categories[name] = Category(name=name)
    db.add(categories[name])
db.flush() # assigns ids without committing
