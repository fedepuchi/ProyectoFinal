
from flask import Blueprint, request, jsonify
from controllers import (crear_taller, editar_taller, eliminar_taller,registrar_estudiante)
from models import Workshop

workshops_bp = Blueprint("workshops", __name__)

# GET /workshops
@workshops_bp.route("/workshops", methods=["GET"])
def get_workshops():
    talleres = Workshop.query.all()
    return jsonify([t.as_dict() for t in talleres])

# GET /workshops/<id>
@workshops_bp.route("/workshops/<int:id>", methods=["GET"])
def get_workshop(id):
    taller = Workshop.query.get(id)
    if not taller:
        return jsonify({"error": "Taller no encontrado"}), 404
    return jsonify(taller.as_dict())

# POST /workshops
@workshops_bp.route("/workshops", methods=["POST"])
def create_workshop():
    data = request.json
    taller = crear_taller(data)
    return jsonify(taller.as_dict()), 201

# PUT /workshops/<id>
@workshops_bp.route("/workshops/<int:id>", methods=["PUT"])
def update_workshop(id):
    data = request.json
    taller = editar_taller(id, data)
    if not taller:
        return jsonify({"error": "Taller no encontrado"}), 404
    return jsonify(taller.as_dict())

# DELETE /workshops/<id>
@workshops_bp.route("/workshops/<int:id>", methods=["DELETE"])
def delete_workshop(id):
    taller = eliminar_taller(id)
    if not taller:
        return jsonify({"error": "Taller no encontrado"}), 404
    return jsonify({"message": "Taller eliminado correctamente"})

# POST /workshops/<id>/register
@workshops_bp.route("/workshops/<int:id>/register", methods=["POST"])
def register_student(id):
    data = request.json
    student_id = data.get("student_id")
    registro = registrar_estudiante(id, student_id)
    return jsonify({"message": "Estudiante registrado", "registro_id": registro.id}), 201