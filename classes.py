#O principal meio de definir objetos em pydantic é através de modelos (modelos são simplesmente classes que herdam de BaseModel).
"""
Dados não confiáveis ​​podem ser passados ​​para um modelo e, após análise e validação , o pydantic garante que os campos da instância
do modelo resultante estarão em conformidade com os tipos de campo definidos no modelo.

Pydantic é principalmente uma biblioteca de análise, não uma biblioteca de validação . A validação é um meio para um fim: construir um modelo que esteja de acordo com os tipos e restrições fornecidos.

Em outras palavras, Pydantic garante os tipos e restrições do modelo de saída, não os dados de entrada.
"""

from datetime import date
from pydantic import BaseModel, ValidationError
from typing import List 


class Autor(BaseModel):
    id: int
    cpf:str
    nome:str
    data_nascimento:str
    endereco_id:int

    class Config:
        orm_mode= True


class Endereco(BaseModel):
    id:int
    cep:str
    logradouro:str
    numero:int
    complemento:str
    cidade_id:int
    estado_id:int
    pais_id:int
    
    class Config:
        orm_mode= True




class Cidade(BaseModel):
    id:int
    sigla:str
    nome:str
        
    class Config:
        orm_mode= True

#CLASSE DE SAÍDA
class Cidade_Out(BaseModel):
    id:int
    sigla:str
    nome:str
        
    class Config:
        orm_mode= True



class Estado(BaseModel):
    id:int
    sigla:str
    nome:str
        
    class Config:
        orm_mode= True



#CLASSE DE SAÍDA
class Estado_Out(BaseModel):
    id:int
    sigla:str
    nome:str
        
    class Config:
        orm_mode= True




class Pais(BaseModel):
    id:int
    sigla:str
    nome:str
    
    class Config:
        orm_mode= True


#CLASSE DE SAÍDA
class Pais_Out(BaseModel):
    id:int
    sigla:str
    nome:str
   

    class Config:
        orm_mode= True




#CLASSE DE SAÍDA
class Endereco_Schema(Endereco):
    autor:Autor
    class Config:
        orm_mode= True


#CLASSE DE SAÍDA
class Endereco_Out(BaseModel):
    cep:str
    logradouro:str
    numero:int
    complemento:str
    cidade:Cidade_Out
    estado: Estado_Out
    pais: Pais_Out
    
    class Config:
        orm_mode= True


#CLASSE DE SAÍDA AUTOR_OUT, A QUAL RECEBE, COMO UMA LISTA, OS DADOS DA CLASSE ENDERECO_OUT
class Autor_Out(BaseModel):
    id: int
    cpf:str
    nome:str
    data_nascimento:str
    endereco:Endereco_Out

    class Config:
        orm_mode= True



    
