# ShopPy — E-Commerce Website

Full-stack e-commerce built with Python Django + PostgreSQL + Docker + Kubernetes + Jenkins CI/CD.

## Tech Stack
- **Backend:** Python 3.11 + Django 4.2
- **Database:** PostgreSQL 15
- **Frontend:** Django Templates (HTML/CSS/JS)
- **Container:** Docker + Docker Compose
- **Web Server:** Nginx (reverse proxy)
- **CI/CD:** Jenkins

---

## OPTION 1: Run Locally (Without Docker)

### Step 1 — Install requirements
```bash
pip install -r requirements.txt
```

### Step 2 — Setup PostgreSQL
```sql
CREATE DATABASE shoppy_db;
CREATE USER shoppy_user WITH PASSWORD 'shoppy_pass';
GRANT ALL PRIVILEGES ON DATABASE shoppy_db TO shoppy_user;
```

### Step 3 — Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4 — Create admin user
```bash
python manage.py createsuperuser
```

### Step 5 — Add sample products
```bash
python seed.py
```

### Step 6 — Start server
```bash
python manage.py runserver
```

Open: http://localhost:8000
Admin: http://localhost:8000/admin

---

## OPTION 2: Run with Docker (Recommended)

### Step 1 — Build and start all containers
```bash
docker-compose up --build
```

### Step 2 — Run migrations inside container
```bash
docker exec -it shoppy_web python manage.py migrate
docker exec -it shoppy_web python manage.py createsuperuser
docker exec -it shoppy_web python seed.py
```

Open: http://localhost (port 80 via Nginx)
Admin: http://localhost/admin

---

## Project Structure
```
ecommerce/
├── ecommerce/          # Django project config
│   ├── settings.py     # All settings
│   ├── urls.py         # Main URL routing
│   └── wsgi.py
├── store/              # Main app
│   ├── models.py       # DB models (Product, Cart, Order...)
│   ├── views.py        # All page logic
│   ├── urls.py         # Store URL routes
│   ├── forms.py        # Checkout + Register forms
│   ├── admin.py        # Admin panel config
│   ├── context_processors.py
│   └── templates/store/
│       ├── home.html
│       ├── product_list.html
│       ├── product_detail.html
│       ├── cart.html
│       ├── checkout.html
│       ├── order_list.html
│       ├── order_detail.html
│       ├── login.html
│       └── register.html
├── templates/
│   └── base.html       # Base layout (navbar, footer)
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
├── Jenkinsfile         # CI/CD pipeline
└── seed.py             # Sample data loader
```

## Pages
| URL | Page |
|-----|------|
| `/` | Home — featured products |
| `/products/` | All products with search + filter |
| `/products/<slug>/` | Product detail page |
| `/cart/` | Shopping cart |
| `/checkout/` | Place order |
| `/orders/` | My orders |
| `/orders/<id>/` | Order detail |
| `/login/` | Login |
| `/register/` | Register |
| `/admin/` | Django admin panel |
