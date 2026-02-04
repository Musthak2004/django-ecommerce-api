# Django Ecommerce API

A simple, modular Ecommerce API built with **Django** and **Django REST Framework**.  
This project includes a custom user model, product catalog, categories, orders, and JWT authentication.  
Perfect for learning, prototyping, or extending into a production-ready ecommerce solution.

---

## 🚀 Features

- Custom User Model (email-based login)
- Product & Category Management
- Orders & Order Items
- JWT Authentication
- Modular App Structure (`accounts`, `store`, `orders`)

---

## 📂 Project Structure

ecommerce_project/
│
├── accounts/ # custom user model, authentication
├── store/ # products, categories
├── orders/ # cart, orders
├── ecommerce_project/
│ ├── settings.py
│ ├── urls.py
│ └── ...

---

## ⚙️ Installation

```bash
# Clone repo
git clone https://github.com/yourusername/django-ecommerce-api.git
cd django-ecommerce-api

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

🔑 API Endpoints
Auth

POST /api/register/

POST /api/login/

Store

GET /api/products/

GET /api/products/<id>/

GET /api/categories/

Orders

POST /api/orders/

GET /api/orders/

🛠️ Tech Stack
Django

Django REST Framework

djangorestframework-simplejwt

📌 Notes
Extendable for payments, shipping, and inventory.

Admin panel supports inline order items.

Built with scalability and clarity in mind.

📜 License
MIT License
