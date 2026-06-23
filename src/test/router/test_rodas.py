from fastapi.testclient import TestClient

from main import app

test=TestClient(app)

rodasRouter = "/api"

def testain():
    response = test.get("/")
    assert response.status_code == 200
    assert response.json() == "Oi"

def testLindo():
    response = test.get(rodasRouter+"/porra")
    assert response.status_code == 200
    assert response.json() == "gozou :3"

def testPost():
    para={"user":"1234"}
    resposta = test.post("lili",headers=para)
    assert resposta.status_code == 201
    assert resposta.json() == "user:1234"

def testdbPost():
    heades={"Content-Type":"application/json"}
    db = {
    "pais": "EUa",
    "name": "testedUser",
    "email": "tested@email.com",
    "password": "sua_senha_secreta"
    }
    resposta=test.post("/api/create",headers=heades,json=db)
    assert resposta.status_code == 201 or resposta.status_code == 200
