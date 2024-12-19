import sqlite3
from typing import Any, Dict

DATABASE = "library.db"

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            author TEXT NOT NULL,
                            published_year INTEGER,
                            genre TEXT,
                            availability INTEGER DEFAULT 1)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS members (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            email TEXT UNIQUE NOT NULL,
                            phone TEXT NOT NULL,
                            membership_date TEXT NOT NULL)''')

def execute_query(query: str, params: tuple = ()) -> Any:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor.fetchall()
