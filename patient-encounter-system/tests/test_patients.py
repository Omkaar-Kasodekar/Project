def test_create_patient(client):
    response = client.post(
        "/patients",
        json={
            "first_name": "Omkaar",
            "last_name": "Kasodekar",
            "email": "ok1@test.com",
            "phone_number": "9999999999",
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "ok1@test.com"
    assert data["id"] > 0


def test_get_patients(client):
    response = client.get("/patients")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
