from flask import Blueprint, request, jsonify
from models import execute_query
from auth import token_required

members_bp = Blueprint("members", __name__)

@members_bp.route("/members", methods=["GET"])
def get_members():
    members = execute_query("SELECT * FROM members")
    return jsonify(members)

@members_bp.route("/members", methods=["POST"])
@token_required
def create_member():
    data = request.json
    execute_query("INSERT INTO members (name, email, phone, membership_date) VALUES (?, ?, ?, ?)",
                  (data["name"], data["email"], data["phone"], data["membership_date"]))
    return jsonify({"message": "Member created"}), 201
