import pytest


@pytest.mark.parametrize(
    "stars, expected_status",
    [
        (0, 400),
        (1, 200),
        (5, 200),
        (6, 400),
    ],
)
def test_update_rating_boundary(api, auth, rating, stars, expected_status):
    rating_id = rating["id"]
    original_stars = rating["stars"]

    body = {"stars": stars}
    res = api.put(
        f"/api/ratings/{rating_id}",
        json=body,
        headers=auth,
    )

    assert res.status_code == expected_status

    if expected_status == 200:
        assert res.json()["stars"] == stars

    else:
        check = api.get(f"/api/ratings/{rating_id}", headers=auth)
        assert check.status_code == 200
        assert check.json()["stars"] == original_stars