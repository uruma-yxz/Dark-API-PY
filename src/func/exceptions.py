from fastapi import HTTPException

def erroHttpNone(conteudo,status:int,detail:dict):
    if conteudo == None:
        raise HTTPException(status_code=status,detail=detail)
    
def erroHttpNot(conteudo,status:int,detail:dict):
    if not conteudo:
        raise HTTPException(status_code=status,detail=detail)
    
def erroHttpUser(conteudo,status:int,detail:dict):
    if conteudo == []:
        raise HTTPException(status_code=status,detail=detail)
    
def erroID(ID):
    if len(ID) == 36:
        return
    else:
        raise HTTPException(status_code=404,detail="ID INVALIDO SUA PUTA")
    
def erroHttp(conteudo,status:int,detail:dict):
        if conteudo == []:
            raise HTTPException(status_code=status,detail=detail)
        if not conteudo:
            raise HTTPException(status_code=status,detail=detail)
        if conteudo == None:
            raise HTTPException(status_code=status,detail=detail)