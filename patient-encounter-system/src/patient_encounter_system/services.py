from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException

from patient_encounter_system.models import Patient, Doctor, Appointment


def create_patient(db: Session, patient: Patient):
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient


def create_doctor(db: Session, doctor: Doctor):
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor


def schedule_appointment(db: Session, appointment: Appointment):
    patient = db.get(Patient, appointment.patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    doctor = db.get(Doctor, appointment.doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    now = datetime.now(timezone.utc)
    if appointment.start_time <= now:
        raise HTTPException(
            status_code=400,
            detail="Cannot schedule appointment in the past",
        )

    new_start = appointment.start_time
    if new_start.tzinfo is None:
        new_start = new_start.replace(tzinfo=timezone.utc)

    new_end = new_start + timedelta(minutes=appointment.duration_minutes)

    existing = (
        db.execute(
            select(Appointment).where(Appointment.doctor_id == appointment.doctor_id)
        )
        .scalars()
        .all()
    )

    for appt in existing:
        existing_start = appt.start_time
        if existing_start.tzinfo is None:
            existing_start = existing_start.replace(tzinfo=timezone.utc)

        existing_end = existing_start + timedelta(minutes=appt.duration_minutes)

        if new_start < existing_end and new_end > existing_start:
            raise HTTPException(
                status_code=409,
                detail="Doctor has overlapping appointment",
            )

    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment
