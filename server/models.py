from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata =MetaData()
db = SQLAlchemy(metadata=metadata)

class Doctor(db.Model):
    __tablename__ = 'doctors'
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.string)
    specialy_id = db.Column(db.Integer, db.Foreignkey("specialties.id"))
    specialty = db.relationship('Specialty', back_populates='doctors')

    doctor_appointments = db.relationship('Appointment', back_populates='doctor')

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.string)

    patient_appointments = db.relationship('Appointment', back_populates='patient')



class Appointment(db.Model):
     __tablename__ = 'appointments'
     id = db.Column(db.Integer, primary_key=True)
     date = db.Column(db.string)
     doctor_id = db.Column(db.Integer, db.Foreignkey('doctors_id'))
     patient_id = db.Column(db.Integer, db.Foreignkey('petiants_id'))

     doctor = db.relationship('Doctor', back_populate='doctor_appointments')
     Patient = db.relationship('Patient', back_populate='patient_appointments')

class Specialty(db.Model):
     __tablename__ = 'specialties'

     id = db.Column(db.integer, primary_key=True)
     name = db.Column(db.string)

     doctors = db.relationship('Doctor',back_populates='specialty',cascade='all, delete')