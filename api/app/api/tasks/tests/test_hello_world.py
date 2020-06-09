import json


def test_hello_world_post(app):
    client = app.test_client()

    res = client.post('/hello-world', json={"msg": "Hello World!"}, follow_redirects=True)
    assert res.status_code == 200
    data = json.loads(res.get_data(as_text=True))
    assert data["msg"] == {"msg": "Hello World!"}


def test_hello_world_get(app):
    client = app.test_client()

    res = client.get('/hello-world')
    assert res.status_code == 200
    data = json.loads(res.get_data(as_text=True))
    assert data["msg"] == "Hello World"
