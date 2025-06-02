from fastapi import FastAPI
from models import Demanda
from database import create_demand, get_all_demanda

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API do Assistente de Demandas no ar."}

@app.post("/demandas/")
def criar_demanda(demanda: Demanda):
    return create_demand(demanda)

@app.get("/demandas/")
def listar_demandas():
    return get_all_demanda()
