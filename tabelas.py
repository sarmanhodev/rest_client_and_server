from database import Base, engine
from sqlalchemy import String,Integer, Column, ForeignKey, Table
from sqlalchemy.orm import relationship



class Autor(Base):
    __tablename__="autor"
    id=Column(Integer, primary_key=True)
    cpf = Column(String(256),nullable= False, unique = True)
    nome = Column(String(256), nullable= False, unique = False)
    data_nascimento = Column(String(256),nullable= False, unique = False)
    endereco_id = Column(Integer,ForeignKey('endereco.id'))
    
    
    #RELATIONSHIPS
    endereco = relationship("Endereco", back_populates = "autor")



class Endereco(Base):
    __tablename__="endereco"
    id=Column(Integer, primary_key=True)
    cep = Column(String(256), nullable= False, unique = False)
    logradouro = Column(String(256), nullable= False, unique = True)
    complemento = Column(String(256), nullable= False, unique = False)
    numero = Column(Integer, nullable= False, unique = False)
    cidade_id = Column(Integer,ForeignKey('cidade.id'))
    estado_id = Column(Integer,ForeignKey('estado.id'))
    pais_id = Column(Integer,ForeignKey('pais.id'))
   

    #RELATIONSHIPS
    autor = relationship("Autor", back_populates = "endereco")
    cidade = relationship("Cidade", back_populates = "endereco")
    estado = relationship("Estado", back_populates = "endereco")
    pais = relationship("Pais", back_populates = "endereco")



class Cidade(Base):
    __tablename__="cidade"
    id=Column(Integer, primary_key=True)
    sigla= Column(String(256), nullable= False, unique = False)
    nome = Column(String(256), nullable= False, unique = False)
    
    
    #RELATIONSHIPS
    endereco = relationship("Endereco", back_populates = "cidade")
    

class Estado(Base):
    __tablename__="estado"
    id=Column(Integer, primary_key=True)
    sigla= Column(String(256), nullable= False, unique = False)
    nome = Column(String(256), nullable= False, unique = False)
    
    
    #RELATIONSHIPS
    endereco = relationship("Endereco", back_populates = "estado")
 
class Pais(Base):
    __tablename__="pais"
    id=Column(Integer, primary_key=True)
    sigla= Column(String(256), nullable= False, unique = False)
    nome = Column(String(256), nullable= False, unique = False)
    
   
    #RELATIONSHIPS
    endereco = relationship("Endereco", back_populates = "pais")
    