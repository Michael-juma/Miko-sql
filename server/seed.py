from app import app
from models import db, Doctor, Patient, Appointment, Specialty

# Wrap DB actions inside app context
with app.app_context():
    # Drop and recreate all tables
    db.drop_all()
    db.create_all()

    # Create specialties
    cardiology = Specialty(name='Cardiology')
    pediatrics = Specialty(name='Pediatrics')
    surgery = Specialty(name='Surgery')

    db.session.add_all([cardiology, pediatrics, surgery])
    db.session.commit()

    # Create doctors
    dr_smith = Doctor(name='Dr. Smith', specialty=cardiology)
    dr_jones = Doctor(name='Dr. Jones', specialty=pediatrics)
    dr_adams = Doctor(name='Dr. Adams', specialty=surgery)

    db.session.add_all([dr_smith, dr_jones, dr_adams])
    db.session.commit()

    # Create patients
    john_doe = Patient(name='John Doe')
    jane_doe = Patient(name='Jane Doe')

    db.session.add_all([john_doe, jane_doe])
    db.session.commit()

    # Create appointments
    appt1 = Appointment(date='2025-06-15', doctor=dr_smith, patient=john_doe)
    appt2 = Appointment(date='2025-06-16', doctor=dr_jones, patient=jane_doe)

    db.session.add_all([appt1, appt2])
    db.session.commit()

    print(" Seed data inserted successfully!")
