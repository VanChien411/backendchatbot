from flask import Blueprint, request, jsonify
from data.connect import connect_to_database

role_blueprint = Blueprint('roles', __name__)

# Thêm một role mới
@role_blueprint.route('/roles', methods=['POST'])
def add_role():
    connection = connect_to_database()
    if connection:
        data = request.json
        role_name = data['role_name']

        cursor = connection.cursor()
        sql = "INSERT INTO role (role_name) VALUES (%s)"
        values = (role_name,)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Role added successfully"}), 201
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin tất cả role
@role_blueprint.route('/roles', methods=['GET'])
def get_all_roles():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM role")
        roles = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(roles), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin của một role dựa trên role_id
@role_blueprint.route('/roles/<int:role_id>', methods=['GET'])
def get_role(role_id):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM role WHERE role_id = %s"
        cursor.execute(sql, (role_id,))
        role = cursor.fetchone()
        cursor.close()
        connection.close()
        if role:
            return jsonify(role), 200
        else:
            return jsonify({"error": "Role not found"}), 404
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Cập nhật thông tin của một role dựa trên role_id
@role_blueprint.route('/roles/<int:role_id>', methods=['PUT'])
def update_role(role_id):
    connection = connect_to_database()
    if connection:
        data = request.json
        role_name = data.get('role_name', '')

        cursor = connection.cursor()
        sql = "UPDATE role SET role_name=%s WHERE role_id=%s"
        values = (role_name, role_id)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Role updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Xóa một role dựa trên role_id
@role_blueprint.route('/roles/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM role WHERE role_id=%s"
        values = (role_id,)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Role deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500
