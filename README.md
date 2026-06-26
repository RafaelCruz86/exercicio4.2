# Exercício 4.2 — MCP Server Local

Servidor MCP local que atua como intermediário entre um agente de IA e a API REST do Exercício 4.1 (TODO list).

## Arquitetura

```
Agente / LLM ──MCP──▶ servidor_mcp.py ──HTTP──▶ API 4.1 (porta 8000)
```

## Ferramentas expostas

| Ferramenta | Parâmetros | Descrição |
|---|---|---|
| `criar_tarefa` | `titulo: str` | POST `/tarefas` — cria uma nova tarefa |
| `listar_tarefas` | — | GET `/tarefas` — retorna todas as tarefas |

## Como executar

**Terminal A — subir a API do exercício 4.1:**
```bash
uvicorn app.main:app --port 8000
```

**Terminal B — rodar o cliente de teste:**
```bash
pip install -r requirements.txt
python cliente_teste.py
```

## Saída esperada

```json
{
  "tools": ["criar_tarefa", "listar_tarefas"],
  "criar_resultado": {"id": 1, "titulo": "tarefa via mcp", "concluida": false},
  "listar_resultado": [{"id": 1, "titulo": "tarefa via mcp", "concluida": false}]
}
```

## Decisões de implementação

- Utilizado `FastMCP` da biblioteca `mcp` por oferecer decoradores simples para expor funções Python como tools MCP.
- O cliente HTTP `httpx` foi escolhido por ser síncrono e leve, adequado para chamadas dentro das tools.
- O MCP abstrai do agente todos os detalhes HTTP: método, URL, headers e serialização JSON ficam encapsulados no servidor, o agente só conhece o nome e os parâmetros da tool.
