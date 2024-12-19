from flask import request

def paginate(items: list, page: int, per_page: int) -> dict:
    start = (page - 1) * per_page
    end = start + per_page
    total_pages = (len(items) + per_page - 1) // per_page
    return {
        "items": items[start:end],
        "total_pages": total_pages,
        "current_page": page
    }
