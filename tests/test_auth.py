def test_register_user(client):
    response = client.post(
        "/api/v1/users/",
        json={
            "email": "test@example.com",
            "password": "123456",
            "full_name": "Test User",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data
    assert "password" not in data  # không trả về password


def test_register_duplicate_email(client):
    client.post(
        "/api/v1/users/",
        json={
            "email": "dup@example.com",
            "password": "123456",
        },
    )
    response = client.post(
        "/api/v1/users/",
        json={
            "email": "dup@example.com",
            "password": "abcdef",
        },
    )
    assert response.status_code == 400


def test_login_success(client):
    client.post(
        "/api/v1/users/",
        json={
            "email": "login@example.com",
            "password": "123456",
        },
    )
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "login@example.com",
            "password": "123456",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data


def test_login_wrong_password(client):
    client.post(
        "/api/v1/users/",
        json={
            "email": "wrong@example.com",
            "password": "123456",
        },
    )
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "wrong@example.com",
            "password": "sai_mat_khau",
        },
    )
    assert response.status_code == 401
