

def test_create_user(client):
    data = {"email": "testuser@nofoobar.com",
            "password": "1234"}
    response = client.post("/user", json=data)
    assert response.status_code == 201
    assert response.json()["data"]["email"] == "testuser@nofoobar.com"
    assert response.json()["data"]["is_active"] == True
