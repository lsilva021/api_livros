# Api de Doaçao de Livros

Essa é uma API simples feita com Flask e SQLite3 para fins de estudo da escola Vai Na Web, ela permite cadastrar e listar livros doados.

## Como rodar o projeto

1. Faça o clone do repositório:
```bash
git clone <URL_DO_REPOSITORIO>
cd nome-do-projeto
```


2. Crie um ambiente virtual (obrigatório):
```bash
python -m venv venv
source venv/Scripts/activate
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

> A api está disponível em http: https://127.0.

## Endpoints

### POST /doar

Endpoint para cadastrar um novo livro

**Formato de envio dos dados**
```json
{
    "titulo":"50 Dols de dívida",
    "categoria":"Finanças",
    "autor":"Fernando Polia",
    "image_url":"https://example.com"
}
```

**Resposta 201 (Created)**
```json
{
    "mensagem":"Livro cadastrado com sucesso"
}
```

---

### GET /livros

Retorna todos os livros cadastrado em nossa API.

***Resposta (200)**
```json
{
    "id":"1",
    "titulo":"50 Dols de dívida",
    "categoria":"Finanças",
    "autor":"Fernando Polia",
    "image_url":"https://example.com"
}
```
---
![alt text](image.png)