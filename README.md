# 🖥️ AssetPulse - Sistema de Telemetria e Gestão de Ativos de TI

O **AssetPulse** é uma solução leve de inventário e monitoramento de ativos desenvolvida em Python. O sistema é composto por um agente coletor (*collector*) que roda nos endpoints da rede local e envia telemetria em tempo real para uma API RESTful centralizada (*FastAPI*), persistindo o histórico das máquinas em banco de dados SQLite.

---

## 🚀 Funcionalidades

- **Coleta Automatizada de Métricas:**
  - Identificação de máquina: *Hostname*, endereço IP local e Sistema Operacional.
  - Telemetria de hardware: Consumo percentual de CPU e utilização de memória RAM.
- **API REST Backend:**
  - Endpoint para recepção periódica de dados de telemetria.
  - Documentação interativa Swagger/OpenAPI integrada.
- **Persistência de Dados:**
  - Armazenamento local rápido e independente via SQLite.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Framework Web / API:** [FastAPI](https://fastapi.tiangolo.com/)
- **Servidor ASGI:** [Uvicorn](https://www.uvicorn.org/)
- **Monitoramento do Sistema:** [psutil](https://github.com/giampaolo/psutil)
- **Requisições HTTP:** [Requests](https://requests.readthedocs.io/)
- **Banco de Dados:** SQLite3

---

## 📂 Estrutura do Repositório

```text
assetpulse/
│
├── backend/
│   └── main.py          # API FastAPI e gerenciamento do banco de dados
│
├── collector/
│   └── agent.py         # Agente coletor de hardware e envio de telemetria
│
├── .gitignore           # Exclusões de arquivos temporários e binários
├── requirements.txt     # Dependências do ecossistema Python
└── README.md            # Documentação técnica do projeto.

Como executar o projeto
# Clone o repositório
git clone [https://github.com/jdadventista-hue/assetpulse-ti.git](https://github.com/jdadventista-hue/assetpulse-ti.git)

# Acesse a pasta do projeto
cd assetpulse-ti

# Instale as dependências necessárias
pip install -r requirements.txt

2. Iniciar o Servidor Backend (FastAPI)
Em um terminal, inicie a API:

Bash
uvicorn backend.main:app --reload
A API estará ativa em: http://127.0.0.1:8000

Documentação interativa (Swagger UI): http://127.0.0.1:8000/docs

3. Executar o Agente Coletor
Abra outro terminal e execute o script do agente para iniciar a coleta:

Bash
python collector/agent.py
O agente passará a capturar as métricas da máquina local e a disparar requisições para a API.

👤 Autor
Desenvolvido por Jefferson Douglas.

Focado em automação para TI, suporte técnico e desenvolvimento de software.

