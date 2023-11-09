from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session


DATABASE_URL = "sqlite:///./FondoFamiliar.db"  # Nombre del archivo de la base de datos SQLite

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



# Función para obtener una instancia de sesión de base de datos por solicitud
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
