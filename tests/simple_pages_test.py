"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/pythonflask">Python-Flask</a>' in response.data
    assert b'<a class="nav-link" href="/cicd">CICD</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200

def test_request_git(client):
    """This makes the index page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_docker(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_pythonflask(client):
    """This makes the index page"""
    response = client.get("/python-flask")
    assert response.status_code == 200
    assert b"Python-Flask" in response.data

def test_request_cicd(client):
    """This makes the index page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"CICD" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404