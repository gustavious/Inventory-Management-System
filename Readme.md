# Inventory Management System

This project is developed to manage Superbeauty's inventory of computers, laptops, servers, or any other equipment. It provides basic functionalities for adding, editing, deleting, and assigning equipment to users.

## Requirements

- Python 3.11+
- Django 5.0+
- djangorestframework 3.14+

## Installation

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/gustavious/inventory-management.git
    ```

2. Navigate to the project directory:

    ```
    cd superbeautyassesment
    ```

3. Make sure to use an environment with the dependencies mentioned above. You can create a venv and install the dependencies with the following commands:

    ```
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```


## Configuration

1. Perform the necessary migrations to set up the SQLite database:

    ```
    python manage.py migrate
    ```

2. Create a superuser to access the admin panel or use the one that's already created: (user: admin, password: admin)

    ```
    python manage.py createsuperuser
    ```

3. Start the development server:

    ```
    python manage.py runserver
    ```

4. Access the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in using the superuser credentials.

## Features

- **Equipment Management:** Allows adding, editing, and deleting equipment from the inventory, including fields like reference, brand, processor, memory, disk, and type.
- **Equipment Assignment:** Enables assigning equipment to users, recording the assignment and delivery dates.
- **Custom Admin Views:** Provides custom admin views for listing equipment and equipment assigned to users.
- **API for Equipment Query:** Offers an API to query the list of equipment.

## Testing

The project includes unit tests for the main models and views. You can run these tests with the command:

    ```
    python manage.py test inventory
    ```

Hope you enjoy it! 😊
```