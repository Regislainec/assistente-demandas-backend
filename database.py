from models import Demanda
import sqlite3

def create_demand(demanda: Demanda):
    conn = sqlite3.connect("demandas.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS demandas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            descricao TEXT,
            nome_responsavel TEXT,
            email_responsavel TEXT,
            prioridade TEXT,
            status TEXT,
            solicitante TEXT,
            delegado TEXT,
            prazo_entrega TEXT,
            prazo_estimado TEXT,
            data_conclusao TEXT,
            reajuste_necessario INTEGER,
            justificativa_reajuste TEXT
        )
    """)
    cursor.execute("""
        INSERT INTO demandas (titulo, descricao, nome_responsavel, email_responsavel, prioridade, status,
                              solicitante, delegado, prazo_entrega, prazo_estimado, data_conclusao,
                              reajuste_necessario, justificativa_reajuste)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        demanda.titulo,
        demanda.descricao,
        demanda.nome_responsavel,
        demanda.email_responsavel,
        demanda.prioridade,
        demanda.status,
        demanda.solicitante,
        demanda.delegado,
        demanda.prazo_entrega,
        demanda.prazo_estimado,
        demanda.data_conclusao,
        int(demanda.reajuste_necessario),
        demanda.justificativa_reajuste
    ))
    conn.commit()
    conn.close()
    return {"mensagem": "Demanda criada com sucesso"}

def get_all_demanda():
    conn = sqlite3.connect("demandas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM demandas")
    colunas = [column[0] for column in cursor.description]
    resultados = cursor.fetchall()
    conn.close()
    return [dict(zip(colunas, row)) for row in resultados]
