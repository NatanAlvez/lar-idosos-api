# lar-idosos-api
Aplicação em Python com FastAPI para acompanhamento de Idosos. 

### Instalação do Python

```
sudo apt install python3.12
```

### Criação do ambiente virtual

Dentro da pasta do projeto configure o ambiente de acordo com as seguintes instruções:

```
sudo apt install python3.12-venv python3.12-dev
python3.12 -m venv venv
```

### Ativando ambiente virtual
Distruibuição Linux:
```
source venv/bin/activate
```

Windows:
```
venv\Scripts\activate
```

### Instalando bibliotecas necessárias para o projeto

Método obsoleto, mas ainda funcional:

```
pip install -r requirements.txt
```

Dê preferência ao arquivo `pyproject.toml` para instalar as dependências do projeto,
pois ele contém as versões exatas das bibliotecas utilizadas.

```
pip install -e .
pip install -e .[dev]
```

### Instalando Docker
    
Distribuição Linux:

Execute o comando abaixo para instalar o Docker como super usuário:
```
curl -fsSL https://get.docker.com/ | sh
```

Após a instalação, adicione seu usuário ao grupo do Docker para ter permissão de executarcomandos 
Docker sem ser super usuário:
```
sudo usermod -aG docker $USER
```

Ou visite https://docs.docker.com/get-started/ e veja outras formas de instalação.

Windows:

Requer a instalação do Docker Desktop.
```
https://docs.docker.com/docker-for-windows/install/
```

### Executando o projeto

Para executar o projeto, execute o comando abaixo:
```
docker-compose up --build
```

### Criando o arquivo .env
Crie o arquivo `.env` na raiz do projeto com a configuração abaixo, substituindo "exemplo" pelos dados reais do banco de dados:

```
DATABASE_NAME=exemplo
DATABASE_USER=exemplo
DATABASE_HOST=exemplo
DATABASE_PORT=exemplo
DATABASE_PASSWORD=exemplo
TIMEZONE=America/Sao_Paulo
DATABASE_URL=postgresql://exemplo:exemplo@exemplo:5432/exemplo
```

### Executar testes

Para executar os testes, execute o comando abaixo na raiz do projeto:

```
pytest
```

Para verificar a cobertura dos testes, execute o comando abaixo:

```
pytest --cov=app
```  
