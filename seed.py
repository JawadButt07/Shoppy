"""
Run this once to add sample products:
  python seed.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Category, Product

categories = [
    {'name': 'Electronics', 'slug': 'electronics', 'description': 'Gadgets and devices'},
    {'name': 'Clothing', 'slug': 'clothing', 'description': 'Fashion and apparel'},
    {'name': 'Books', 'slug': 'books', 'description': 'Books and literature'},
    {'name': 'Home & Kitchen', 'slug': 'home-kitchen', 'description': 'Home essentials'},
]

products = [
    {'name': 'Wireless Bluetooth Headphones', 'slug': 'wireless-bluetooth-headphones', 'category': 'electronics', 'price': '59.99', 'stock': 25, 'description': 'Premium sound quality with 30hr battery life, noise cancellation, and foldable design.'},
    {'name': 'Mechanical Gaming Keyboard', 'slug': 'mechanical-gaming-keyboard', 'category': 'electronics', 'price': '89.99', 'stock': 15, 'description': 'RGB backlit mechanical keyboard with tactile switches, perfect for gaming and typing.'},
    {'name': 'USB-C Fast Charger 65W', 'slug': 'usb-c-fast-charger-65w', 'category': 'electronics', 'price': '29.99', 'stock': 50, 'description': 'Universal 65W fast charger compatible with laptops, phones, and tablets.'},
    {'name': 'Wireless Mouse', 'slug': 'wireless-mouse', 'category': 'electronics', 'price': '24.99', 'stock': 40, 'description': 'Ergonomic wireless mouse with silent click, 12 months battery life.'},
    {'name': 'Cotton Casual T-Shirt', 'slug': 'cotton-casual-t-shirt', 'category': 'clothing', 'price': '14.99', 'stock': 100, 'description': '100% pure cotton, available in multiple colors, pre-shrunk fabric.'},
    {'name': 'Slim Fit Jeans', 'slug': 'slim-fit-jeans', 'category': 'clothing', 'price': '39.99', 'stock': 60, 'description': 'Classic slim fit denim jeans with stretch fabric for comfort.'},
    {'name': 'Hooded Sweatshirt', 'slug': 'hooded-sweatshirt', 'category': 'clothing', 'price': '34.99', 'stock': 45, 'description': 'Warm fleece hoodie with kangaroo pocket, perfect for cool weather.'},
    {'name': 'Python Crash Course', 'slug': 'python-crash-course', 'category': 'books', 'price': '19.99', 'stock': 30, 'description': 'Best-selling beginner Python programming book. Learn Python from scratch with real projects.'},
    {'name': 'Clean Code', 'slug': 'clean-code', 'category': 'books', 'price': '22.99', 'stock': 20, 'description': 'Robert C. Martin\'s classic guide to writing maintainable, readable software.'},
    {'name': 'The DevOps Handbook', 'slug': 'the-devops-handbook', 'category': 'books', 'price': '24.99', 'stock': 18, 'description': 'How to create world-class agility, reliability, and security in technology organizations.'},
    {'name': 'Non-Stick Frying Pan', 'slug': 'non-stick-frying-pan', 'category': 'home-kitchen', 'price': '32.99', 'stock': 35, 'description': '28cm non-stick ceramic frying pan, dishwasher safe, works on all hob types.'},
    {'name': 'Electric Kettle 1.7L', 'slug': 'electric-kettle-1-7l', 'category': 'home-kitchen', 'price': '27.99', 'stock': 28, 'description': 'Rapid boil 1.7L kettle with auto shut-off and boil-dry protection.'},
]

print("Creating categories...")
cat_objects = {}
for c in categories:
    obj, created = Category.objects.get_or_create(slug=c['slug'], defaults=c)
    cat_objects[c['slug']] = obj
    print(f"  {'Created' if created else 'Exists'}: {obj.name}")

print("\nCreating products...")
for p in products:
    cat_slug = p.pop('category')
    p['category'] = cat_objects[cat_slug]
    obj, created = Product.objects.get_or_create(slug=p['slug'], defaults=p)
    print(f"  {'Created' if created else 'Exists'}: {obj.name}")

print("\nDone! Open http://localhost:8000 to see your store.")
print("Admin panel: http://localhost:8000/admin/")
