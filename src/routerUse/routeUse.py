from fastapi import APIRouter, HTTPException
from typing import Annotated
from src.Model.TableUser import TableUser
from fastapi import Depends,Request
from fastapi import Response
from src.func.ratelimite import limiter
from src.func.exceptions import erroHttpNot,erroHttpNone,erroHttpUser,erroHttp,erroID
from sqlmodel import Session, select
from src.func.ratelimite import limiter
from src.dbMotor.database import engine

router = APIRouter(prefix="/api",tags=["api"])

def getSessionDB():
    with Session(engine) as SessionON:
        yield SessionON

SessionDB = Annotated[Session,Depends(getSessionDB)]

@router.get("/")
@limiter.limit("3/3 minute")
def gozor(request:Request)-> str:
    return "Meu amor"

@router.get("/porra")
@limiter.limit("2/minute")
def juju(request:Request) -> str:
    return "gozou :3" 

@router.post("/create",response_model=TableUser,status_code=201)
@limiter.limit("1/30 minute")
def creadeUsers(us:TableUser,go:SessionDB,request:Request):
    go.add(us)
    go.commit()
    return Response(status_code=201)

@router.get("/user",response_model=list[TableUser],status_code=200)
@limiter.limit("3/minute")
def getUsers(db:SessionDB,request:Request):
    users = db.exec(select(TableUser)).all()
    return users

@router.get("/id/{iduser}",response_model=TableUser,status_code=200)
@limiter.limit("3/minute")
def getUsersfromID(db:SessionDB,iduser:str,request:Request):
    erroID(iduser)
    dados = db.get(TableUser,iduser)
    erroHttp(dados,status=404,detail={"erro":404,"meng":"User Not Fount"})
    return dados

@router.get("/buscar",response_model=list[TableUser])
@limiter.limit("3/minute")
def buscaName(db:SessionDB,nome:str,request:Request):
    buscar= select(TableUser).where(TableUser.name == nome)
    user = db.exec(buscar).all()
    erroHttp(user,status=404,detail={"erro":404,"meng":"User Not Fount"})
    return user

@router.patch("/changeName/{idUser}",response_model=TableUser,status_code=201)
@limiter.limit("3/minute")
def mudaName(idUser:str,db:SessionDB,nome:str,request:Request):
    erroID(idUser)
    user = db.get(TableUser,idUser)
    user.name = nome
    db.add(user)
    db.commit()
    return Response(status_code=201)

@router.delete("/exluir/{idUser}",response_model=TableUser,status_code=200)
@limiter.limit("3/minute")
def deleteUser(db:SessionDB,idUser:str,request:Request):
    user = db.get(TableUser,idUser)
    erroHttp(user,status=404,detail={"erro":404,"meng":"User Not Fount"})
    db.delete(user)
    db.commit()
    return Response(status_code=200)