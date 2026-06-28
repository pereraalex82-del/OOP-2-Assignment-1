# Library Management System

A modern FastAPI-based REST API for managing a library's books, authors, members, and book loans.

## Overview

This application provides a comprehensive solution for managing library operations, including:
- **Book Management**: Create, read, and manage books with ISBN and descriptions
- **Author Management**: Track authors and their published books
- **Member Management**: Register and manage library members
- **Loan Tracking**: Monitor book loans with due dates and return tracking

## Project Structure

```
library/
├── app/
│   ├── crud.py              # Database CRUD operations
│   ├── database.py          # Database configuration and session management
│   ├── main.py              # FastAPI application setup
│   ├── models.py            # SQLAlchemy ORM models
│   ├── schemas.py           # Pydantic request/response schemas
│   └── routers/
│       ├── authors.py       # Author endpoints
│       └── books.py         # Book endpoints
├── requirements.txt         # Python dependencies
├── seed_db.py              # Database seeding script
└── library.db              # SQLite database file
```

## Tech Stack

- **Framework**: FastAPI
- **Server**: Uvicorn
- **Database**: SQLite + SQLAlchemy ORM
- **Data Validation**: Pydantic

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup Steps

1. **Clone or extract the project**
   ```bash
   cd library
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   python seed_db.py
   ```
   This creates the SQLite database and populates it with sample data.

## Running the Application

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Access the API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Books
- `GET /books` - Get all books (with pagination)
- `POST /books` - Create a new book
- `GET /books/{book_id}` - Get book details with author information

### Authors
- `GET /authors` - Get all authors (with pagination)
- `POST /authors` - Create a new author
- `GET /authors/{author_id}` - Get author details with their books

## Database Models

### Author
- `id`: Integer (Primary Key)
- `name`: String
- `bio`: String (Optional)
- **Relationships**: One-to-many with Books

### Book
- `id`: Integer (Primary Key)
- `title`: String
- `description`: String (Optional)
- `isbn`: String (Unique)
- `author_id`: Integer (Foreign Key)
- **Relationships**: Many-to-one with Author, One-to-many with Loans

### Member
- `id`: Integer (Primary Key)
- `fullname`: String
- `email`: String (Unique)
- `membership_date`: Date
- `is_active`: Boolean
- **Relationships**: One-to-many with Loans

### Loan
- `id`: Integer (Primary Key)
- `book_id`: Integer (Foreign Key)
- `member_id`: Integer (Foreign Key)
- `loan_date`: Date
- `due_date`: Date
- `return_date`: Date (Optional)
- **Relationships**: Many-to-one with Book and Member

## Usage Examples

### Create an Author
```bash
curl -X POST "http://localhost:8000/authors" \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Austen", "bio": "English novelist"}'
```

### Create a Book
```bash
curl -X POST "http://localhost:8000/books" \
  -H "Content-Type: application/json" \
  -d '{"title": "Pride and Prejudice", "isbn": "978-0141439518", "author_id": 1}'
```

### Retrieve All Books
```bash
curl "http://localhost:8000/books"
```

### Get Book Details
```bash
curl "http://localhost:8000/books/1"
```

## Project Purpose

This is an OOP 2 Assignment showcasing:
- Object-oriented database modeling with SQLAlchemy
- RESTful API design principles
- Proper separation of concerns (routers, models, schemas, CRUD)
- Database relationships and foreign keys
- Pydantic schema validation

## License

This project is created for educational purposes.
