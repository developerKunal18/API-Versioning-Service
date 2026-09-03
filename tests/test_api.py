from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_v1_contract():
    client = app.test_client()
    response = client.get("/api/v1/products")
    assert response.status_code == 200
    assert response.json["version"] == "v1"
    assert "products" in response.json
    assert "count" not in response.json

def test_v2_contract():
    client = app.test_client()
    response = client.get("/api/v2/products")
    body = response.json
    assert response.status_code == 200
    assert body["version"] == "v2"
    assert body["count"] == len(body["data"])
    assert body["data"][0]["currency"] == "INR"

def test_unknown_route():
    client = app.test_client()
    response = client.get("/does-not-exist")
    assert response.status_code == 404
    assert response.json["error"] == "resource_not_found"
