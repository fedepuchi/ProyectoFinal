from models import Workshop, Student, Registration
from database import db

def crear_taller(data):
    taller = Workshop(**data)
    db.session.add(taller)
    db.session.commit()
    return taller

def editar_taller(id, data):
    taller = Workshop.query.get(id)
    if taller:
        for key, value in data.items():
            setattr(taller, key, value)
        db.session.commit()
    return taller

def eliminar_taller(id):
    taller = Workshop.query.get(id)
    if taller:
        db.session.delete(taller)
        db.session.commit()
    return taller

def registrar_estudiante(workshop_id, student_id):
    registro = Registration(
        workshop_id=workshop_id,
        student_id=student_id
    )
    db.session.add(registro)
    db.session.commit()
    return registro
