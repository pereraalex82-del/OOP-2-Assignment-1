from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date

# Base shared properties
class AuthorBase(BaseModel):
    name: str
    bio: Optional[str] = None

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# Book shared properties
class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    isbn: str
    author_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# Member shared properties
class MemberBase(BaseModel):
    fullname: str
    email: str
    membership_date: date
    is_active: bool = True

class MemberCreate(MemberBase):
    pass

class Member(MemberBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# Loan shared properties
class LoanBase(BaseModel):
    book_id: int
    member_id: int
    loan_date: date
    due_date: date
    return_date: Optional[date] = None

class LoanCreate(LoanBase):
    pass

class Loan(LoanBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# Relationship Schemas
class AuthorWithBooks(Author):
    books: List[Book] = []

class BookWithAuthor(Book):
    author: Author
