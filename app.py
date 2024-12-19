from flask import Flask
from models import init_db
from routes.books import books_bp
from routes.members import members_bp

app = Flask(__name__)

init_db()

app.register_blueprint(books_bp, url_prefix="/api")
app.register_blueprint(members_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
