from flask import Blueprint, request, jsonify
from models.task_model import Task
from views.task_view import render_task_detail, render_task_list
from flask_jwt_extended import get_jwt_identity
from utils.decorators import roles_required, jwt_required

# Crear un blueprint para el controlador de tareas
task_bp = Blueprint("task", __name__)

# Ruta para obtener la lista de tareas
@task_bp.route("/tasks", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "member"])
def get_tasks():
    tasks = Task.get_all()
    return jsonify(render_task_list(tasks))

# Ruta para obtener una tarea específica por su ID
@task_bp.route("/tasks/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "member"])
def get_task(id):
    task = Task.get_by_id(id)
    if task:
        return jsonify(render_task_detail(task))
    return jsonify({"error": "Tarea no encontrada"})

# Ruta para crear una nueva tarea
@task_bp.route("/tasks", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_task():
    data = request.json
    title = data.get("title")
    description = data.get("description")
    status = data.get("status")
    created_at = data.get("created_at")
    assigned_to=data.get("assigned_to")
    
    if not (title and description and status and created_at):
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    task = Task(title=title, description=description, status=status, created_at=created_at, assigned_to=assigned_to)
    task.save()
    return jsonify(render_task_detail(task)), 201
    
# Ruta para actualizar una tarea existente por su ID
@task_bp.route("/tasks/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_task(id):
    task = Task.get_by_id(id)
    if not task:
        return jsonify({"error": "Dulce no encontrado"}), 404
    
    data = request.json
    title = data.get("title")
    description = data.get("description")
    status = data.get("status")
    created_at = data.get("created_at")
    assigned_to=data.get("assigned_to")
    
    task.update(title=title, description=description, status=status, created_at=created_at, assigned_to=assigned_to)
    
    return jsonify(render_task_detail(task))

# Ruta para eliminar una tarea existente por su ID
@task_bp.route("/tasks/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_task(id):
    task = Task.get_by_id(id)
    if not task:
        return jsonify({"error": "Tarea no encontrada"}), 404
    
    task.delete()
    return "", 204