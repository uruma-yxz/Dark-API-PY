from src.func.id import idGerador
from sqlmodel import Field, SQLModel

class TableUser(SQLModel,table=True):
    __tablename__= "users"
    id:str = Field(default_factory=idGerador,primary_key=True,max_length=36)
    pais:str = Field(default="Russia",min_length=2,max_length=20)
    name:str = Field(min_length=3,max_length=30)
    email:str = Field(min_length=5,max_length=255)
    password:str = Field(min_length=8,max_length=255)