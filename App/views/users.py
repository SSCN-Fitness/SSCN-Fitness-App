from flask import Blueprint, request, jsonify
from App.controllers import create_user, get_user_by_username, get_user, get_all_users, update_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def create_new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    user = create_user(username, password)
    return jsonify(user.serialize()), 201

@user_bp.route('/users/<string:username>', methods=['GET'])
def get_user_by_username_api(username):
    user = get_user_by_username(username)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.serialize()), 200

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = get_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.serialize()), 200

@user_bp.route('/users', methods=['GET'])
def get_all_users_api():
    users = get_all_users()
    if not users:
        return jsonify({'message': 'No users found'}), 200
    return jsonify([user.serialize() for user in users]), 200

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user_api(user_id):
    username = request.json.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400
    result = update_user(user_id, username)
    if not result:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'message': 'User updated successfully'}), 200