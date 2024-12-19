# Library Management System

## **Overview**
This is a simple Flask-based API for managing books and library members. It supports CRUD operations, search functionality, pagination, and token-based authentication.

---

## **How to Run the Project**

### 1. **Setup**
- Clone the repository:
  ```bash
  git clone <repository-url>
  cd library_management
Ensure Python 3.x is installed on your system.


2. Initialize the Database
Create the SQLite database and tables:
bash
python -c "from models import init_db; init_db()"

3. Start the Application
Run the Flask app:
python app.py
The server will start at http://127.0.0.1:5000.


4. Test the Endpoints
Use tools like Postman, cURL, or a web browser.
Examples:
Get all books: http://127.0.0.1:5000/api/books
Add a book (with token): Send a POST request to http://127.0.0.1:5000/api/books with the header Authorization: your-secret-token

Design Choices
1. Database
SQLite was chosen for simplicity and ease of setup.
Two tables (books and members) are used to manage the library data.
2. API Structure
CRUD operations for books and members are divided into two separate modules (routes/books.py and routes/members.py) to keep the code modular and maintainable.
3. Authentication
A simple token-based authentication system is implemented using a hardcoded token in auth.py.
4. Pagination
Custom pagination logic is provided in utils.py to handle paginated responses without third-party libraries.
5. Constraints
The project avoids third-party libraries to adhere to the requirements, using only Flask and Python’s standard libraries.



Assumptions and Limitations
Assumptions
Authentication:
The token is hardcoded in auth.py as SECRET_TOKEN. Replace it with a secure token for production use.
Search Functionality:
Search is case-insensitive and supports partial matches for title and author.
Limitations
Database:
SQLite is not suitable for production environments with high traffic or concurrent users.
Error Handling:
Limited error handling is implemented (e.g., invalid data or server issues).
Authentication:
No dynamic user management; only a single hardcoded token is used.
Scalability:
Designed for simplicity and may require modifications for larger-scale deployments.



Future Enhancements
Add user-based authentication with login and role-based access control.
Use a more robust database like PostgreSQL for scalability.
Improve error handling and validation.
Add automated API documentation.




Let me know if you need further adjustments!


To test your API in the browser or tools like Postman, append the appropriate endpoint path to the base URL http://127.0.0.1:5000. Here are some examples:

Books API
Get All Books:
http://127.0.0.1:5000/api/books
Search Books by Title or Author:
http://127.0.0.1:5000/api/books?title=SomeTitle
http://127.0.0.1:5000/api/books?author=SomeAuthor


Create a Book (Requires Token):
Use a tool like Postman or cURL to send a POST request with JSON data:
POST http://127.0.0.1:5000/api/books
Headers:
Authorization: your-secret-token
Body:
{
    "title": "Book Title",
    "author": "Author Name",
    "published_year": 2021,
    "genre": "Fiction"
}


Members API
Get All Members:
http://127.0.0.1:5000/api/members
Create a Member (Requires Token):

Use a tool like Postman or cURL to send a POST request with JSON data:
POST http://127.0.0.1:5000/api/members
Headers:
Authorization: your-secret-token
Body:
{
    "name": "J D",
    "email": "j.d@exam.com",
    "phone": "1234567890",
    "membership_date": "2024-12-19"
}
