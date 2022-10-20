# """This test the homepage"""

# def test_request_main_menu_links(client):
#     """This makes the index page"""
#     response = client.get("/")
#     assert response.status_code == 200
#     assert b'<a class="nav-link" href="/git">Git</a>' in response.data
#     assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
#     assert b'<a class="nav-link" href="/pythonflask">Python-Flask</a>' in response.data
#     assert b'<a class="nav-link" href="/cicd">CICD</a>' in response.data

#     assert b'<a class="dropdown-item" href="/OOP">OOP</a>' in response.data
#     assert b'<a class="dropdown-item" href="/solid">SOLID</a>' in response.data
#     assert b'<a class="dropdown-item" href="/pylint">Pylint</a>' in response.data
#     assert b'<a class="dropdown-item" href="/AAA-testing">AAA Testing</a>' in response.data


# def test_request_index(client):
#     """This makes the index page"""
#     response = client.get("/")
#     assert response.status_code == 200
#     assert b"Home" in response.data

# def test_request_git(client):
#     """This makes the git page"""
#     response = client.get("/git")
#     assert response.status_code == 200
#     assert b"Git" in response.data

# def test_request_docker(client):
#     """This makes the docker page"""
#     response = client.get("/docker")
#     assert response.status_code == 200
#     assert b"Docker" in response.data

# def test_request_pythonflask(client):
#     """This makes the client page"""
#     response = client.get("/pythonflask")
#     assert response.status_code == 200
#     assert b"Python-Flask" in response.data

# def test_request_cicd(client):
#     """This makes the cicd page"""
#     response = client.get("/cicd")
#     assert response.status_code == 200
#     assert b"CICD" in response.data

# def test_request_page_not_found(client):
#     """This makes the not found page"""
#     response = client.get("/page5")
#     assert response.status_code == 404




# def test_request_oop(client):
#     """This makes the OOP page"""
#     response = client.get("/OOP")
#     assert response.status_code == 200
#     assert b"OOP" in response.data

# def test_request_aaa(client):
#     """This makes the AAA testing page"""
#     response = client.get("/AAA-testing")
#     assert response.status_code == 200
#     assert b"AAA-testing" in response.data

# def test_request_solid(client):
#     """This makes the client page"""
#     response = client.get("/solid")
#     assert response.status_code == 200
#     assert b"solid" in response.data

# def test_request_pylint(client):
#     """This makes the pylint page"""
#     response = client.get("/pylint")
#     assert response.status_code == 200
#     assert b"pylint" in response.data
