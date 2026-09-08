import sqlite3
from datetime import datetime
from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title="AssetPulse API",
    description="API de Gestão de Ativos e Telemetria de TI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def init_db():
    conn = sqlite3.connect("assetpulse.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS telemetry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hostname TEXT NOT NULL,
            ip_address TEXT NOT NULL,
            os_name TEXT NOT NULL,
            cpu_usage REAL NOT NULL,
            ram_usage REAL NOT NULL,
            disk_usage REAL NOT NULL,
            recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

class TelemetryPayload(BaseModel):
    hostname: str
    ip_address: str
    os_name: str
    cpu_usage: float
    ram_usage: float
    disk_usage: float

@app.post("/api/telemetry", status_code=201)
def receive_telemetry(data: TelemetryPayload):
    conn = sqlite3.connect("assetpulse.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO telemetry (hostname, ip_address, os_name, cpu_usage, ram_usage, disk_usage)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (data.hostname, data.ip_address, data.os_name, data.cpu_usage, data.ram_usage, data.disk_usage))
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Telemetria registrada com sucesso."}

@app.get("/api/telemetry")
def get_telemetry():
    conn = sqlite3.connect("assetpulse.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, hostname, ip_address, os_name, cpu_usage, ram_usage, disk_usage, recorded_at
        FROM telemetry
        ORDER BY recorded_at DESC
        LIMIT 50
    """)
    rows = cursor.fetchall()
    conn.close()
    
    results = []
    for row in rows:
        results.append({
            "id": row[0],
            "hostname": row[1],
            "ip_address": row[2],
            "os_name": row[3],
            "cpu_usage": row[4],
            "ram_usage": row[5],
            "disk_usage": row[6],
            "recorded_at": row[7]
        })
    return results

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)