from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Modalidade(Base):
    __tablename__ = "modalidades"

    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True, nullable=False) 
    descricao = Column(String, nullable=True) 

    matriculas = relationship("Matricula", back_populates="modalidade", cascade="all, delete-orphan")

    def __init__(self, nome, descricao=""):
        self.nome = nome
        self.descricao = descricao

    def exibir_detalhes(self):
        print(f"Modalidade: {self.nome}, Descrição: {self.descricao if self.descricao else 'Sem descrição'}")
