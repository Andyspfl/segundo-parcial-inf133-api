from flask import Blueprint, request, jsonify
from models.user_model import User
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from views.user_view import render_user_detail, render_user_list
from utils.decorators import roles_required, jwt_required

user_bp = Blueprint("user", __name__)

@user_bp.route("/users", methods=["GET"])
#@roles_required(roles=["admin", "user"])
@jwt_required
def get_users():
    users = User.get_all()
    return jsonify(render_user_list(users))

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    roles = data.get("role")

    if not name or not password:
        return jsonify({"error": "Se requieren nombre de usuario y contraseña"}), 400

    existing_user = User.find_by_user(name)
    if existing_user:
        return jsonify({"error": "El nombre de usuario ya está en uso"}), 400

    new_user = User(name, email, password,roles)
    new_user.save()

    return jsonify({"message": "Usuario creado exitosamente"}), 201


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    name = data.get("user")
    email = data.get("email")
    password = data.get("password")

    user = User.find_by_user(email)
    if user and check_password_hash(user.password, password):
        # Si las credenciales son válidas, genera un token JWT
        access_token = create_access_token(identity={"name":name,"roles":user.roles})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401
    
    
@user_bp.route("/users/<int:id>", methods=["PUT"])
@roles_required(roles=("admin"))
@jwt_required
def update_user(id):
    user = User.get_by_id(id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    data = request.json 
    
    user = data.get("user")
    email = data.get("email")
    password = data.get("password")
    roles = data.get("roles")
    
    user.update(user=user, email=email, password=password, roles=roles)
    
    return jsonify(render_user_detail(user))

# Ruta para eliminar una tarea existente por su ID
@user_bp.route("/users/<int:id>", methods=["DELETE"])
@roles_required(roles=["admin"])
@jwt_required
def delete_user(id):
    user = User.get_by_id(id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    
    user.delete()
    return "", 204