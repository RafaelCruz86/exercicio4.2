import logging
import httpx
from mcp.server.fastmcp import FastMCP

logging.disable(logging.CRITICAL)

API = "http://localhost:8000"
mcp = FastMCP("tarefas-mcp")

@mcp.tool()
def criar_tarefa(titulo: str) -> str:
    """Cria uma tarefa na API e devolve o objeto criado."""
    resp = httpx.post(f"{API}/tarefas", json={"titulo": titulo}, timeout=10)
    resp.raise_for_status()
    return resp.text

@mcp.tool()
def listar_tarefas() -> str:
    """Lista todas as tarefas da API."""
    resp = httpx.get(f"{API}/tarefas", timeout=10)
    resp.raise_for_status()
    return resp.text

if __name__ == "__main__":
    mcp.run()
