import uuid

def test_duplicate_username_is_refused(api):
    username = "duplicate-user"
    password = "Pizza-2026"

    first = api.post(
        "/api/users",
        json={"username": username, "password": password},
    )
    assert first.status_code == 201

    second = api.post(
        "/api/users",
        json={"username": username, "password": password},
    )
    assert second.status_code == 400
    assert second.json() == {"error": "username already taken"}


def test_wrong_password_is_refused(api):
    username = "wrong-password-" + uuid.uuid4().hex[:12]
    password = "Pizza-2026"

    user = {"username": username, "password": password}
    created = api.post("/api/users", json=user)
    assert created.status_code == 201

    res = api.post(
        "/api/users/token/login",
        json={"username": username, "password": "Wrong-Password"},
    )
    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}

def test_empty_username_is_refused(api):
    res = api.post(
        "/api/users",
        json={"username": "", "password": "Pizza-2026"},
    )
    assert res.status_code == 400
    assert res.json() == {"error": "username field is empty"}