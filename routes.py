from database import db
from models import Registration, Workshop
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from controllers import (crear_taller, editar_taller, eliminar_taller,registrar_estudiante)
from models import Workshop
from datetime import datetime
workshops_bp = Blueprint("workshops", __name__)

# GET /workshops
@workshops_bp.route("/workshops", methods=["GET"])
def get_workshops():
    talleres = Workshop.query.all()
    return jsonify([t.as_dict() for t in talleres])

@workshops_bp.route("/workshops/new", methods=["GET"])
def new_workshop():
    return render_template("workshop_form.html", taller=None)


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
    data = {
        "nombre": request.form["nombre"],
        "descripcion": request.form.get("descripcion"),
        "fecha": request.form.get("fecha"),
        "hora": request.form.get("hora"),
        "lugar": request.form.get("lugar"),
        "categoria": request.form.get("categoria")
    }

    taller = Workshop(**data)
    db.session.add(taller)
    db.session.commit()

    return redirect("/workshops/new")


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


@workshops_bp.route("/workshops/<int:id>/register", methods=["POST"])
def register_student(id):
    student_id = request.form["student_id"]
    registro = Registration(
        workshop_id=id,
        student_id=student_id,
        fecha_registro=datetime.now().strftime("%d/%m/%Y %H:%M")
    )
    db.session.add(registro)
    db.session.commit()
    return redirect("/workshops")  



@workshops_bp.route("/admin")
def admin_panel():
    talleres = Workshop.query.all()  # o como se llame en tu proyecto
    return render_template("admin_panel.html", talleres=talleres)