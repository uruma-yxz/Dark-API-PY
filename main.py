import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append("/code")

from src.dbMotor.database import engine
from fastapi import Response,Request,Depends
from fastapi import Header
from fastapi.responses import HTMLResponse
from src.Model.TableUser import TableUser
from src.routerUse import routeUse
from typing import Annotated
from fastapi.responses import JSONResponse
from src.func.ratelimite import limiter
from fastapi import FastAPI, HTTPException
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from sqlmodel import Session, select
import uvicorn

app = FastAPI(docs_url=None,redoc_url=None)
app.state.limiter = limiter
@app.exception_handler(RateLimitExceeded)
def erro(request:Request,exc:RateLimitExceeded):
    return JSONResponse(
        content={"Rate Limite":"Esta Muito Rapido Espera Sua Puta :3"}
    )

@app.get("/docs")
def documentao():
    with open("src/front/index.html","r",encoding="utf-8") as html:
        htmlSave = html.read()
    return HTMLResponse(content=htmlSave,status_code=200)

@app.get("/")
def main():
    return "Oi"

@app.get("/rr")
@limiter.limit("3/minute")
def testRate(request:Request):
    return "ok"

@app.post("/lili",status_code=201)
def mm(user_tk:str = Header("1234")):
    return f"user:{user_tk}"

app.include_router(routeUse.router)

if __name__=="__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)