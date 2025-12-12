from database import db

class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    fecha = db.Column(db.String(20))
    hora = db.Column(db.String(20))
    lugar = db.Column(db.String(100))
    categoria = db.Column(db.String(50))

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workshop_id = db.Column(db.Integer, db.ForeignKey('workshop.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    fecha_registro = db.Column(db.String(20))