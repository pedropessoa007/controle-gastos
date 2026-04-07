import json
import os

ARQUIVO = "gastos" \
".json"


def carregar_gastos():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_gastos(gastos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(gastos, f, ensure_ascii=False, indent=2)


def adicionar_gasto(descricao, valor):
    if not descricao or not descricao.strip():
        raise ValueError("Descrição não pode ser vazia.")
    if valor <= 0:
        raise ValueError("Valor deve ser maior que zero.")
    gastos = carregar_gastos()
    gasto = {"descricao": descricao.strip(), "valor": round(valor, 2)}
    gastos.append(gasto)
    salvar_gastos(gastos)
    return gasto


def listar_gastos():
    return carregar_gastos()


def remover_gasto(indice):
    gastos = carregar_gastos()
    if indice < 0 or indice >= len(gastos):
        raise IndexError("Índice inválido.")
    removido = gastos.pop(indice)
    salvar_gastos(gastos)
    return removido


def total_gastos():
    gastos = carregar_gastos()
    return round(sum(g["valor"] for g in gastos), 2)
