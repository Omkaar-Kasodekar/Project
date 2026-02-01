def test_create_doctor(client):
    response = client.post(
        "/doctors",
        json={
            "full_name": "Omkaar",
            "specialization": "Neurology",
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["full_name"] == "Omkaar"
    assert data["id"] > 0


def test_get_doctors(client):
    response = client.get("/doctors")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
