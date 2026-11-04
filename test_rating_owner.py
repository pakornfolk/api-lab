def test_other_user_cannot_read_rating(api, rating, other_auth, auth):
    rating_id = rating["id"]
    res = api.get(f"/api/ratings/{rating_id}", headers=other_auth)
    print("Other user read status:", res.status_code)
    assert 400 <= res.status_code <= 499

    check = api.get(f"/api/ratings/{rating_id}", headers=auth)
    assert check.status_code == 200
    assert check.json()["stars"] == rating["stars"]


def test_other_user_cannot_update_rating(api, rating, other_auth, auth):
    rating_id = rating["id"]
    res = api.put(
        f"/api/ratings/{rating_id}",
        json={"stars": 5},
        headers=other_auth,
    )
    print("Other user update status:", res.status_code)
    assert 400 <= res.status_code <= 499

    check = api.get(f"/api/ratings/{rating_id}", headers=auth)
    assert check.status_code == 200
    assert check.json()["stars"] == rating["stars"]


def test_other_user_cannot_delete_rating(api, rating, other_auth, auth):
    rating_id = rating["id"]
    res = api.delete(f"/api/ratings/{rating_id}", headers=other_auth)
    print("Other user delete status:", res.status_code)
    assert 400 <= res.status_code <= 499

    check = api.get(f"/api/ratings/{rating_id}", headers=auth)
    assert check.status_code == 200
    assert check.json()["stars"] == rating["stars"]