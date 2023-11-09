from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    fecha_ingreso = Column(Date, nullable=True)
    fecha_salida = Column(Date, nullable=True)
    gf_id = Column(Integer, ForeignKey("grupos_familiares.gf_id"))
    cuota = Column(Float, nullable=False)
    
    aportes = relationship("Aportes", back_populates="usuarios")
    abonos = relationship("Abonos", back_populates="usuarios")
    prestamos = relationship("Prestamos", back_populates="usuarios")
    
class GrupoFamiliar(Base):
    __tablename__ = "grupos_familiares"

    gf_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    
class Aportes(Base):
    __tablename__ = "aportes"

    Ap_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("usuarios.user_id"))
    fechaAporte = Column(Date, nullable=False)
    valor = Column(Float)

    usuarios = relationship("Usuario", back_populates="aportes")
    
class FondoFamiliar(Base):
    __tablename__ = "fondofamiliar"

    id = Column(Integer, primary_key=True, index=True)
    monto_total = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)
    
class Abonos(Base):
    __tablename__ = "abonos"

    Ab_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("usuarios.user_id"), nullable=False)
    fecha = Column(Date, nullable=False)
    interes_a_la_fecha = Column(Float, nullable=False)
    valor_abono = Column(Float, nullable=False)
    saldo_fecha = Column(Float)
    Pr_id = Column(Integer, ForeignKey("prestamos.Pr_id"))

    usuarios = relationship("Usuario", back_populates="abonos")
    prestamos = relationship("Prestamos", back_populates="abonos")
    
class Prestamos(Base):
    __tablename__ = "prestamos"

    Pr_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("usuarios.user_id"), nullable=False)
    monto = Column(Float, nullable=False)
    interes = Column(Float, nullable=False)
    fechainicio = Column(Date)
    fechafin = Column(Date)
    
    usuarios = relationship("Usuario", back_populates="prestamos")
    abonos = relationship("Abonos", back_populates="prestamos")