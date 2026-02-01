from datetime import datetime, timedelta, timezone


def create_patient_and_doctor(client):
    patient = client.post(
        "/patients",
        json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@test.com",
            "phone_number": "8888888888",
        },
    ).json()

    doctor = client.post(
        "/doctors",
        json={
            "full_name": "Dr Who",
            "specialization": "General",
        },
    ).json()

    return patient["id"], doctor["id"]


def test_create_appointment(client):
    patient_id, doctor_id = create_patient_and_doctor(client)

    start_time = (datetime.now(timezone.utc) + timedelta(days=1)).isoformat()

    response = client.post(
        "/appointments",
        json={
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "start_time": start_time,
            "duration_minutes": 30,
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["patient_id"] == patient_id
    assert data["doctor_id"] == doctor_id


def test_appointment_overlap(client):
    patient_id, doctor_id = create_patient_and_doctor(client)

    start_time = datetime.now(timezone.utc) + timedelta(days=1)

    client.post(
        "/appointments",
        json={
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "start_time": start_time.isoformat(),
            "duration_minutes": 60,
        },
    )

    response = client.post(
        "/appointments",
        json={
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "start_time": (start_time + timedelta(minutes=30)).isoformat(),
            "duration_minutes": 30,
        },
    )

    assert response.status_code == 409
    assert response.json()["detail"] == "Doctor has overlapping appointment"


def test_get_appointments(client):
    response = client.get("/appointments")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
