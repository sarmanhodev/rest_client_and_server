from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from classes import *
from database import SessionLocal
import tabelas
from typing import List
from sqlalchemy.orm import joinedload


app = FastAPI() #VARIÁVEL QUE RECEBE A INSTÂNCIA DA FASTAPI

db = SessionLocal() #VARIÁVEL QUE RECEBE A INSTÂNCIA DO SESSIONLOCAL, DO BANCO DE DADOS

templates = Jinja2Templates(directory="templates") #VARIÁVEL QUE RECEBE A INSTÂNCIA DO JINJA2, PARA GERAR OS TEMPLATES


#Você receberá uma resposta informando que os dados são inválidos contendo o corpo recebido
@app.exception_handler(RequestValidationError)
async def validation_error(request:Request,exc:RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail":exc.errors(),"body":exc.body})
    )



@app.get("/", status_code=status.HTTP_200_OK)
async def hello():
    """
    **Boas vindas**
    """

    ola=str("Seja bem-vindo, usuário!")
    print("\n"+str(ola)+"\n")
    return ola


#POST AUTOR
@app.post("/autor/", response_model=Autor, status_code=status.HTTP_201_CREATED)
async def add_autor(autor: Autor):
    """
    Cria um novo registro na tabela **Autor**
    
    - **id: int**
    - **cpf:str**
    - **nome:str**
    - **data_nasciment:str**
    - **endereco_id:int**
    
    """ 

    novo_autor = tabelas.Autor(cpf = autor.cpf, nome = autor.nome, data_nascimento = autor.data_nascimento, endereco_id=autor.endereco_id)
    db.add(novo_autor)
    db.commit()
    
  
   
    print("\nAutor cadastrado com sucesso\n")

    return novo_autor


#DELETA UM REGISTRO DA TABELA AUTOR
@app.delete("/autor/delete/{id}", response_model=Autor, status_code=status.HTTP_200_OK)
async def deleta_autor(id:int):
    """
    Após efetuar a busca de um determinado autor através de seu **Id**, esta função apaga registro existente no banco
    """

    autor_delete = db.query(tabelas.Autor).filter(tabelas.Autor.id==id).first()

    if autor_delete is None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')
    
    db.delete(autor_delete)
    db.commit()

    print("REGISTRO EXCLUIDO")
    return autor_delete


#ATUALIZANDO REGISTRO DA TABELA AUTOR
@app.put("/autor/update/{id}",response_model=Autor_Out,status_code=status.HTTP_200_OK)
async def atualiza_autor(id:int,autor:Autor_Out):
    """
    Após efetuar a busca de um determinado autor através de seu **Id**, seu registro poderá ser atualizado
    """
    autor_update = db.query(tabelas.Autor).filter(tabelas.Autor.id==id).options(joinedload(tabelas.Autor.endereco)).first()

    if autor_update == None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')

    autor_update.name=autor.cpf
    autor_update.email=autor.nome
    autor_update.senha=autor.data_nascimento

    db.commit()

    
    print("\nDados atualizados com sucesso!")
    return autor_update

#GET RETORNA TODOS OS REGISTROS EM UM TEMPLATE HTML
@app.get("/autores/",response_model= List[Autor_Out], status_code=status.HTTP_200_OK)
async def get_autores_html(request:Request):
    """
      - Retorna os valores registrados na tabela **Autor** em um template HTML
    
    """
    #VARIÁVEL AUTOR, QUE RECEBE TODOS OS REGISTROS DA TABELA AUTOR
    autor = db.query(tabelas.Autor).order_by(tabelas.Autor.id).options(joinedload(tabelas.Autor.endereco)).all()
    #SE NÃO HOUVER NENHUM REGISTRO NA TABELA, RETORNARÁ UMA MENSAGEM AVISANDO
    if autor == None:
        print("\nNenhum registro encontrado")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum registro encontrado")
    

    #RETORNA TODOS OS DADOS NO TEMPLATE todos.html.  
    return templates.TemplateResponse("todos.html",{"request": request,"autor": autor})




#GET RETORNA TODOS OS REGISTROS EM UM ARQUIVO JSON
@app.get("/autores/json",response_model= List[Autor_Out], status_code=status.HTTP_200_OK)
async def get_autores():
    """
      - Retorna os valores registrados na tabela **Autor** em formato JSON
    
    """
 
    autor = db.query(tabelas.Autor).order_by(tabelas.Autor.id).options(joinedload(tabelas.Autor.endereco)).all()

    if autor == None:
        print("\nNenhum registro encontrado")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum registro encontrado")
    
         
    return autor


#GET AUTOR ID
@app.get("/autor/id/{id}", response_model = Autor_Out)
async def get_autor_id(id:int):
    """
    - Realiza a busca por um autor através de seu **ID**
    
    """
    autor_id = db.query(tabelas.Autor).filter(tabelas.Autor.id==id).first()

    return autor_id



#GET AUTOR CPF
@app.get("/autor/cpf/{cpf}", response_model = Autor_Out, response_class=HTMLResponse)
async def get_autor_cpf(cpf:str, request:Request):
    """
    - Realiza a busca por um autor através de seu **CPF**
    
    """
    #VARIÁVEL autor_cpf QUE RECEBE OS DADOS DE UM DETERMINADO AUTOR, APÓS A BUSCA PELO SEU CPF
    autor_cpf = db.query(tabelas.Autor).filter(tabelas.Autor.cpf==cpf).first()
    #SE NÃO HOUVER NENHUM REGISTRO NA TABELA, COM UM DETERMINADO CPF, RETORNARÁ UMA MENSAGEM DE ERRO
    if autor_cpf == None:
        print("\nNenhum registro encontrado")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum registro encontrado")
    
    #RETORNA O RESULTADO DA PESQUISA POR CPF NO TEMPLATE detalhes.html
    return templates.TemplateResponse("detalhes.html",{"request": request,"autor": autor_cpf})




#POST ENDEREÇO
@app.post("/endereco/", response_model=Endereco, status_code=status.HTTP_201_CREATED)
async def add_endereco(endereco: Endereco):
    """
    - Cria um novo registro na tabela **Endereco**
    
    - **id:int**
    - **cep:str**
    - **logradouro:str**
    - **numero:int**
    - **complemento:str**
    - **cidade_id:int**
    - **estado_id:int**
    - **pais_id:int**
      
    """

    novo_endereco=tabelas.Endereco(cep=endereco.cep, logradouro=endereco.logradouro,complemento = endereco.complemento, numero=endereco.numero,
    cidade_id = endereco.cidade_id, estado_id=endereco.estado_id, pais_id=endereco.pais_id)
    db.add(novo_endereco)
    db.commit()
    
  
   
    print("\nEndereço cadastrado com sucesso\n")

    return novo_endereco


#DELETA UM REGISTRO DA TABELA ENDEREÇO
@app.delete("/endereco/delete/{id}", response_model=Endereco, status_code=status.HTTP_200_OK)
async def deleta_endereco(id:int):
    """
    Após efetuar a busca de um determinado endereço através de seu **Id**, esta função apaga registro existente no banco
    """

    endereco_delete = db.query(tabelas.Endereco).filter(tabelas.Endereco.id==id).first()

    if endereco_delete is None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')
    
    db.delete(endereco_delete)
    db.commit()

    print("REGISTRO EXCLUIDO")
    return endereco_delete


#ATUALIZANDO REGISTRO DA TABELA ENDEREÇO
@app.put("/endereco/update/{id}",response_model=Endereco,status_code=status.HTTP_200_OK)
async def atualiza_endereco(id:int,endereco:Endereco):
    """
    Após efetuar a busca de um determinado endereco através de seu **Id**, seu registro poderá ser atualizado
    """
    endereco_update = db.query(tabelas.Endereco).filter(tabelas.Endereco.id==id).first()

    if endereco_update == None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')

    endereco_update.name=endereco.cep
    endereco_update.email=endereco.logradouro
    endereco_update.senha=endereco.numero
    endereco_update.senha=endereco.complemento

    db.commit()

    
    print("\nDados atualizados com sucesso!")
    return endereco_update


#GET ENDEREÇOS
@app.get("/enderecos/", response_model = List[Endereco_Out], status_code=status.HTTP_200_OK)
async def get_endereco():
    """
    - Retorna todos os registros da tabela **Endereco**
    """
    endereco = db.query(tabelas.Endereco).options(joinedload(tabelas.Endereco.cidade), joinedload(tabelas.Endereco.estado),\
    joinedload(tabelas.Endereco.pais)).all()

    if endereco == None:
        print("\nNenhum registro encontrado")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum registro encontrado")

    return endereco 



#GET BUSCA CEP
@app.get("/endereco/{cep}", response_model = Endereco_Schema)
async def get_endereco_cep(cep:str):
    """
    - Realiza a busca por um endereço através de seu **CEP**
    
    """
    endereco_id = db.query(tabelas.Endereco).filter(tabelas.Endereco.cep==cep).first()

    return endereco_id


#POST CIDADE
@app.post("/cidade/", response_model=Cidade, status_code=status.HTTP_201_CREATED)
async def add_cidade(cidade: Cidade):
    """
    Cria um novo registro na tabela **Cidade**
    
    - **id: int**
    - **sigla: str**
    - **nome: str** 
    
    
    """

    nova_cidade=tabelas.Cidade(sigla= cidade.sigla ,nome= cidade.nome)
    db.add(nova_cidade)
    db.commit()
    
    print("\nid: "+str(nova_cidade.id))
    print("sigla: "+str(nova_cidade.sigla))
    print("nome: "+str(nova_cidade.nome))
   
    print("\nCidade cadastrada com sucesso\n")

    return nova_cidade


#DELETA UM REGISTRO DA TABELA CIDADE
@app.delete("/cidade/delete/{id}", response_model=Cidade, status_code=status.HTTP_200_OK)
async def deleta_cidade(id:int):
    """
    Após efetuar a busca de uma determinada cidade através de seu **Id**, esta função apaga registro existente no banco
    """

    cidade_delete = db.query(tabelas.Cidade).filter(tabelas.Cidade.id==id).first()

    if cidade_delete is None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')
    
    db.delete(cidade_delete)
    db.commit()

    print("REGISTRO EXCLUIDO")
    return cidade_delete



#ATUALIZANDO REGISTRO DA TABELA CIDADE
@app.put("/cidade/update/{id}",response_model=Cidade,status_code=status.HTTP_200_OK)
async def atualiza_cidade(id:int,cidade:Cidade):
    """
    Após efetuar a busca de uma determinada cidade através de seu **Id**, seu registro poderá ser atualizado
    """
    cidade_update = db.query(tabelas.Cidade).filter(tabelas.Cidade.id==id).first()

    if cidade_update == None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')

    cidade_update.name=cidade.sigla
    cidade_update.email=cidade.nome
    
    db.commit()

    
    print("\nDados atualizados com sucesso!")
    return cidade_update



#GET CIDADES
@app.get("/cidades/", response_model=List[Cidade], status_code=status.HTTP_200_OK)
async def get_cidades():
    """
   - Retorna todos os registros da tabela **CIDADE**
    """
    cidades = db.query(tabelas.Cidade).all()

    if cidades == None:
        print("\nNenhum registro encontrado")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum registro encontrado")

    return cidades


#POST ESTADO
@app.post("/estado/", response_model=Estado, status_code=status.HTTP_201_CREATED)
async def add_estado(estado: Estado):
    """
    Cria um novo registro na tabela **Estado**
    
    - **id: int**
    - **sigla: str**
    - **nome: str** 
    
    
    """

    novo_estado=tabelas.Estado(sigla= estado.sigla ,nome= estado.nome)
    db.add(novo_estado)
    db.commit()
    
    print("\nid: "+str(novo_estado.id))
    print("sigla: "+str(novo_estado.sigla))
    print("nome: "+str(novo_estado.nome))
   
    print("\nEstado cadastrado com sucesso\n")

    return novo_estado


#DELETA UM REGISTRO DA TABELA ESTADO
@app.delete("/estado/delete/{id}", response_model=Estado, status_code=status.HTTP_200_OK)
async def deleta_estado(id:int):
    """
    Após efetuar a busca de um determinado estado através de seu **Id**, esta função apaga registro existente no banco
    """

    estado_delete = db.query(tabelas.Estado).filter(tabelas.Estado.id==id).first()

    if estado_delete is None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')
    
    db.delete(estado_delete)
    db.commit()

    print("REGISTRO EXCLUIDO")
    return estado_delete



#ATUALIZANDO REGISTRO DA TABELA ESTADO
@app.put("/estado/update/{id}",response_model=Estado,status_code=status.HTTP_200_OK)
async def atualiza_estado(id:int,estado:Estado):
    """
    Após efetuar a busca de um determinado endereco através de seu **Id**, seu registro poderá ser atualizado
    """
    estado_update = db.query(tabelas.Estado).filter(tabelas.Estado.id==id).first()

    if estado_update == None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')

    estado_update.name=estado.sigla
    estado_update.email=estado.nome
    
    db.commit()

    
    print("\nDados atualizados com sucesso!")
    return estado_update


#GET ESTADOS
@app.get("/estados/",response_model= List[Estado], status_code=status.HTTP_200_OK)
async def get_estados():
    """
    - Retorna todos os registros da tabela **ESTADOS**
    """
 
    estado = db.query(tabelas.Estado).all()

    if estado == None:
        print("\nNenhum registro encontrado")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum registro encontrado")
    
    #total="Total de alunos cadastrados: "+str(len(aluno))
   
    #print("\n"+str(total)+"\n")
    return estado


#POST PAÍS
@app.post("/paises/", response_model=Pais, status_code=status.HTTP_201_CREATED)
async def add_pais(pais: Pais):
    """
    - Cria um novo registro na tabela **País**
    
    - **id: int**
    - **sigla: str**
    - **nome: str** 
    
    
    """

    novo_pais=tabelas.Pais(sigla= pais.sigla ,nome= pais.nome)
    db.add(novo_pais)
    db.commit()
    
    print("\nid: "+str(novo_pais.id))
    print("sigla: "+str(novo_pais.sigla))
    print("nome: "+str(novo_pais.nome))
   
    print("\nPaís cadastrado com sucesso\n")

    return novo_pais

#DELETA UM REGISTRO DA TABELA PAÍS
@app.delete("/pais/delete/{id}", response_model=Pais, status_code=status.HTTP_200_OK)
async def deleta_estado(id:int):
    """
    Após efetuar a busca de um determinado país através de seu **Id**, esta função apaga registro existente no banco
    """

    pais_delete = db.query(tabelas.Pais).filter(tabelas.EstPaisado.id==id).first()

    if pais_delete is None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')
    
    db.delete(pais_delete)
    db.commit()

    print("REGISTRO EXCLUIDO")
    return pais_delete


#ATUALIZANDO REGISTRO DA TABELA PAÍS
@app.put("/pais/update/{id}",response_model=Pais,status_code=status.HTTP_200_OK)
async def atualiza_pais(id:int,pais:Pais):
    """
    Após efetuar a busca de um determinado país através de seu **Id**, seu registro poderá ser atualizado
    """
    pais_update = db.query(tabelas.Pais).filter(tabelas.EstadPaiso.id==id).first()

    if pais_update == None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')

    pais_update.name=pais.sigla
    pais_update.email=pais.nome
    
    db.commit()

    
    print("\nDados atualizados com sucesso!")
    return pais_update


#GET PAÍSES
@app.get("/paises/",response_model= List[Pais], status_code=status.HTTP_200_OK)
async def get_paises():
    """
    - Retorna todos os registros da tabela **País**
    """
 
    pais = db.query(tabelas.Pais).all()

    if pais == None:
        print("\nNenhum registro encontrado")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum registro encontrado")
    
   
    return pais




if __name__ == "__main__":
    app.run(app, host="0.0.0.0", port=8000)