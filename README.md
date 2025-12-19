# ToDo List API

A robust RESTful API for a note-taking application, built with Django REST Framework. This API allows users to register, authenticate via JWT, and perform CRUD operations on their personal notes.

## 🚀 Features

- **User Authentication**: Secure user registration and login using JWT (JSON Web Tokens).
- **CRUD Operations**: Comprehensive Create, Read, Update, and Delete functionality for notes.
- **User Privacy**: Users can only access and manage their own notes.
- **API Documentation**: Clean structure using Django REST Framework's DefaultRouter.

## 🛠️ Technology Stack

- **Backend Framework**: Django & Django REST Framework (DRF)
- **Authentication**: `rest_framework_simplejwt` for JWT authentication
- **Database**: SQLite (default, easily switchable to PostgreSQL/MySQL)

## 📂 API Endpoints

### Authentication
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/register/` | Register a new user |
| `POST` | `/api/token/` | Login to obtain Access & Refresh tokens |
| `POST` | `/api/token/refresh/` | Refresh an expired access token |

### Notes
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/notes/` | Get a list of all your notes |
| `POST` | `/api/notes/` | Create a new note |
| `GET` | `/api/notes/{id}/` | Get details of a specific note |
| `PUT` | `/api/notes/{id}/` | Update an existing note |
| `DELETE` | `/api/notes/{id}/` | Delete a note |

## ⚙️ Setup & Installation

Follow these steps to set up the project locally:

1.  **Clone the Repository**
    ```bash
    git clone <repository_url>
    cd ToDoListAPI
    ```

2.  **Create a Virtual Environment**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install django djangorestframework djangorestframework-simplejwt
    ```

4.  **Run Migrations**
    ```bash
    python manage.py migrate
    ```

5.  **Start the Development Server**
    ```bash
    python manage.py runserver
    ```

The API will be available at `http://127.0.0.1:8000/`.

## 🧪 Testing with Postman (or VS Code Thunder Client)

1.  **Register** a new user at `/api/register/`.
2.  **Login** at `/api/token/` with your credentials to get an `access` token.
3.  **Authorize**:
    *   In your API Request headers, add:
        *   **Key**: `Authorization`
        *   **Value**: `Bearer <your_access_token>`
4.  **Manage Notes**: Use the `/api/notes/` endpoints to create and view your notes!
