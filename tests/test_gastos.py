import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from gastos import adicionar_gasto, listar_gastos, remover_gasto, total_gastos


@pytest.fixture(autouse=True)
def limpar_arquivo():
    if os.path.exists("gastos.json"):
        os.remove("gastos.json")
    yield
    if os.path.exists("gastos.json"):
        os.remove("gastos.json")


def test_adicionar_gasto_valido():
    gasto = adicionar_gasto("Almoço", 25.50)
    assert gasto["descricao"] == "Almoço"
    assert gasto["valor"] == 25.50


def test_adicionar_gasto_valor_negativo():
    with pytest.raises(ValueError):
        adicionar_gasto("Erro", -10)


def test_adicionar_gasto_descricao_vazia():
    with pytest.raises(ValueError):
        adicionar_gasto("", 10)


def test_listar_gastos_vazio():
    assert listar_gastos() == []


def test_remover_gasto_valido():
    adicionar_gasto("Café", 5.00)
    removido = remover_gasto(0)
    assert removido["descricao"] == "Café"


def test_remover_gasto_indice_invalido():
    with pytest.raises(IndexError):
        remover_gasto(99)


def test_total_gastos():
    adicionar_gasto("Almoço", 20.00)
    adicionar_gasto("Café", 5.00)
    assert total_gastos() == 25.00
