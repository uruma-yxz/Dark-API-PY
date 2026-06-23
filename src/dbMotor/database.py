from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine
from dotenv import load_dotenv
import os

load_dotenv()
db = os.getenv("dbloja")

engine = create_engine(db)
