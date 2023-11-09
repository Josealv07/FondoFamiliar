from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Usuario

app = FastAPI()

@app.get("/{number}")
def read_root(number:int):
    return {"Hello": f"{number}"}

@app.get("/usuarios/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(Usuario).filter(Usuario.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


@app.get("/usuarios/")
def consultar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return usuarios