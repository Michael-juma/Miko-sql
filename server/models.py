from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class Doctor(db.Model):
    __tablename__ = 'doctors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    specialty_id = db.Column(db.Integer, db.ForeignKey("specialties.id"))
    
    specialty = db.relationship('Specialty', back_populates='doctors')
    doctor_appointments = db.relationship('Appointment', back_populates='doctor')


class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
    patient_appointments = db.relationship('Appointment', back_populates='patient')


class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    
    doctor = db.relationship('Doctor', back_populates='doctor_appointments')
    patient = db.relationship('Patient', back_populates='patient_appointments')


class Specialty(db.Model):
    __tablename__ = 'specialties'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
    doctors = db.relationship('Doctor', back_populates='specialty', cascade='all, delete')
