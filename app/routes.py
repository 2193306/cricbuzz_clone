from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Simple check for demonstration purposes
    if username == 'username' and password == 'password':
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})
