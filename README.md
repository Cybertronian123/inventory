
# Inventory Management API

This is a backend API built using Django Rest Framework (DRF) for an Inventory Management System. The API supports CRUD operations on inventory items and uses JWT-based authentication to secure access.

## Features:
- JWT Authentication for securing the API.
- CRUD operations on inventory items (Create, Read, Update, Delete).
- Redis caching for frequently accessed items.
- PostgreSQL as the database backend.
- Logging system for monitoring and debugging.
- Unit tests for API functionalities.

## Requirements:
- Python 3.x
- Django 3.x+
- Django Rest Framework
- PostgreSQL
- Redis

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/inventory-api.git
   ```

2. Install dependencies:
   ```bash
   sudo apt install pipx
   ```

   ```bash
   pipx ensurepath
   ```

   ```bash
   pipx install poetry
   ```

   ```bash
   make install
   ```

   ```bash
   mkdir local & \
   cp inventory/project/settings/templates/settings.dev.py ./local/settings.dev.py
   ```

3. Configure PostgreSQL database settings in `project/settings/base.py` under `DATABASES`.

4. Run migrations:
   ```bash
   make migrations
   ```
   ```bash
   make migrate
   ```

5. Start the development server:
   ```bash
   make runserver
   ```

## API Endpoints

### Authentication

The authentication system uses JSON Web Tokens (JWT) for secure access to the API. You must obtain an access token by logging in, and use this token for authorized requests.

#### 1. Register a User
- **URL:** `/api/auth/register/`
- **Method:** `POST`
- **Description:** Registers a new user and returns a JWT token.

**Request Body Example:**
```json
{
   "username": "new_user",
   "email": "user@example.com",
   "password": "newpassword123"
}
```

**Response Example:**
```json
{
   "refresh": "<refresh_token>",
   "access": "<access_token>",
   "username": "new_user"
}
```

#### 2. Login User
- **URL:** `/api/auth/login/`
- **Method:** `POST`
- **Description:** Logs in an existing user and returns a JWT token.

**Request Body Example:**
```json
{
   "username": "new_user",
   "password": "newpassword123"
}
```

**Response Example:**
```json
{
   "refresh": "<refresh_token>",
   "access": "<access_token>"
}
```

#### 3. Refresh Token
- **URL:** `/api/auth/refresh/`
- **Method:** `POST`
- **Description:** Refreshes the access token using the refresh token.

**Request Body Example:**
```json
{
   "refresh": "<refresh_token>"
}
```

**Response Example:**
```json
{
   "access": "<new_access_token>"
}
```

### Items

These endpoints allow you to perform CRUD operations on inventory items. All `items` endpoints are protected by JWT authentication.

#### 1. Create Item
- **URL:** `/api/items/`
- **Method:** `POST`
- **Description:** Creates a new inventory item.

**Request Body Example:**
```json
{
   "name": "Laptop",
   "description": "A high-end gaming laptop",
   "quantity": 10,
   "price": 1500.00
}
```

**Response Example:**
```json
{
   "id": 1,
   "name": "Laptop",
   "description": "A high-end gaming laptop",
   "quantity": 10,
   "price": 1500.00
}
```

#### 2. Read Item
- **URL:** `/api/items/<item_id>/`
- **Method:** `GET`
- **Description:** Retrieves details of an inventory item by its ID.

**Response Example:**
```json
{
   "id": 1,
   "name": "Laptop",
   "description": "A high-end gaming laptop",
   "quantity": 10,
   "price": 1500.00
}
```

#### 3. Update Item
- **URL:** `/api/items/<item_id>/update/`
- **Method:** `PUT`
- **Description:** Updates an existing inventory item.

**Request Body Example:**
```json
{
   "name": "Laptop",
   "description": "Updated description",
   "quantity": 5,
   "price": 1400.00
}
```

**Response Example:**
```json
{
   "id": 1,
   "name": "Laptop",
   "description": "Updated description",
   "quantity": 5,
   "price": 1400.00
}
```

#### 4. Delete Item
- **URL:** `/api/items/<item_id>/delete/`
- **Method:** `DELETE`
- **Description:** Deletes an inventory item by its ID.

**Response Example:**
```json
{
   "message": "Item deleted successfully"
}
```

### Caching

- **Redis Caching** is applied to the `Read Item` endpoint to improve performance for frequently accessed items. Once an item is retrieved, it is stored in Redis for future requests.

### Unit Tests

- Unit tests for the API are included to ensure functionality and error handling.
- To run the tests:
   ```bash
   make test
   ```

### Logging

- A logging system is integrated to monitor API usage, errors, and significant events.
- Logs can be accessed in the console while running the development server.
