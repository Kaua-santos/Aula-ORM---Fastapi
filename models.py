# models é o arquivo onde fica as classes (tabelas)
from sqlalchemy  import Column,Integer,String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base 

# Tabelas curso e aluno (1:N)
class Curso (Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    carga_horaria = Column(String(100), nullable=False, unique=True)
    descricao = Column(String(167))

    alunos = relationship("Aluno", back_populates="cursos")

    def __repr__(self):
        return f"Curso = id: {self.id}- nome: {self.nome} - carga horaria {self.carga_horaria}"
    

class Aluno(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)

    curso_id = Column(Integer, ForeignKey("cursos.id"))

    cursos = relationship("Curso", back_populates="alunos")

    def __repr__(self):
        return f"curso = id {self.id} - nome: {self.nome} - Email: {self.email}"
    