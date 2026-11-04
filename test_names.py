import requests

SITE = "https://quickpizza.grafana.com"


def test_names_are_listed():
    res = requests.get(SITE + "/api/names")
    assert res.status_code == 200
    assert "Margherita" in res.json()["names"]