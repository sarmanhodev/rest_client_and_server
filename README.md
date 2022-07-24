# rest_client_and_server
Trabalho do Grupo 03 - API RestFull

Para ter acesso a funcionalidade da aplicação, é necessária a instalação de um ambiente virtual: Abrir IDE -> Terminal -> pip install venv.
Após a instalação da dependência virtualenv, o usuário irá criar o ambiente virtual em sua pasta: virtualenv env.
Para iniciar a aplicação, no VSCODE, basta abrir a pasta env -> Scripts, selecionar o arquivo activate.ps1 e aguardar a inicialização do ambiente virtual.
Em seguida, serão instaladas as seguintes dependências, dentro da raíz do ambiente virtual, seguindo sempre o mesmo padrão de instalação: .\env\Scripts\pip3 install fastapi
Para este trabalho, foram usadas as seguintes dependências: FastAPI, psycopg2 (PostgreSQL), sqlalchemy, uvicorn (servidor remoto), JINJA2 (renderiza os templates HTML).
Para iniciar a aplicação, o usuário irá digitar o seguinte comando: uvicorn main:app --reload
O uvicorn irá iniciar, dando acesso aos endpoints.
Para acessar a documentação da FastAPI, basta digitar, na barra de endereço do navegador, o endereço: localhost/docs
