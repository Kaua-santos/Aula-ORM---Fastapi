from fastapi import FastAPI 

# iniciar o app fastapi
app = FastAPI(title="Gestão Escolar")


# metodos http: GET - POST - PUT - DELETE
@app.get("/")
def tela_inicial():
    return {"Mensagem": "sistema de gestao escolar "}

# Banco de dados
usuarios = {
    1: {"nome": "Kauã", "idade": 17},
    2: {"nome": "Damas", "idade": 83},
    3: {"nome": "Lohan", "idade": 25},
}

@app.get("/alunos")
def listar_alunos():
    return {"usuarios": usuarios}
