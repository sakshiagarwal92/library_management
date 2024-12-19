from flask import Blueprint, request, jsonify
from models import execute_query
from auth import token_required

books_bp = Blueprint("books", __name__)

@books_bp.route("/books", methods=["GET"])
def get_books():
    query = "SELECT * FROM books"
    filters = []
    params = []
    if "title" in request.args:
        filters.append("title LIKE ?")
        params.append(f"%{request.args['title']}%")
    if "author" in request.args:
        filters.append("author LIKE ?")
        params.append(f"%{request.args['author']}%")
    if filters:
        query += " WHERE " + " AND ".join(filters)
    books = execute_query(query, tuple(params))
    return jsonify(books)

@books_bp.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    book = execute_query("SELECT * FROM books WHERE id = ?", (id,))
    return jsonify(book[0]) if book else jsonify({"error": "Book not found"}), 404

@books_bp.route("/books", methods=["POST"])
@token_required
def create_book():
    data = request.json
    execute_query("INSERT INTO books (title, author, published_year, genre) VALUES (?, ?, ?, ?)",
                  (data["title"], data["author"], data.get("published_year"), data.get("genre")))
    return jsonify({"message": "Book created"}), 201
