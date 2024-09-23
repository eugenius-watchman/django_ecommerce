Storefront2 E-commerce App (RESTful E-Commerce App)
An Overview

Storefront2 is a production-grade, RESTful e-commerce application designed to manage all aspects of an online store. This project includes a fully-featured backend for handling products, customers, orders, and more, providing the necessary tools to build a complete e-commerce platform.
Features

    RESTful API: A fully scalable API for managing products, orders, customers, and inventory.
    Authentication & Permissions: Secure user authentication with role-based access control for various operations.
    Product Management: Create, read, update, and delete products, categories, and collections.
    Order Management: Handle customer orders, order items, and payment processing.
    Filtering, Pagination, and Search: Customizable filters and paginated results for product listings and orders.
    Admin Interface: An intuitive Django admin interface for managing store operations.
    Event-Driven Architecture: Signals used for handling automatic notifications and updates within the app.

Tech Stack

    Django: Python-based web framework for rapid development.
    Django REST Framework (DRF): For building the API layer.
    MySQL: Database for storing application data.
    Docker (optional): For containerization and easy deployment.

Future Enhancements

    Payment gateway integration
    Customer reviews and ratings
    Advanced analytics and reporting

Clone
git clone https://github.com/eugenius-watchman/storefront2.git

Required dependencies
pipenv install

Data base migrations
python manage.py migrate

Start development server
python manage.py runserver



