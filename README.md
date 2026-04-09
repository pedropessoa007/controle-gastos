# Controle de Gastos Pessoais

![CI](https://github.com/pedropessoa007/controle-gastos/actions/workflows/ci.yml/badge.svg)

## Descrição do problema

Muitas pessoas têm dificuldade em controlar seus gastos do dia a dia,
o que pode levar a um desequilíbrio financeiro e um endividamento.

## Proposta da solução

Aplicação de linha de comando (CLI) simples para registrar, listar,
remover e totalizar gastos pessoais, ajudando o usuário a ter
consciência do que está gastando.

## Público-alvo

Qualquer pessoa que queira organizar melhor suas finanças pessoais.

## Funcionalidades

- Adicionar um gasto com descrição e valor
- Listar todos os gastos registrados
- Remover um gasto pelo índice
- Ver o total de gastos

## Tecnologias utilizadas

- Python 3.14
- pytest (testes automatizados)
- ruff (linting)

## Instalação

1. Clone o repositório:
   git clone https://github.com/pedropessoa007/controle-gastos.git
   cd controle-gastos

2. Instale as dependências:
   py -m pip install -r requirements.txt

## Execução

    cd src
    py app.py

## Rodando os testes

    py -m pytest tests/ -v

## Rodando o lint

    py -m ruff check src/

## Versão atual

1.0.0

## Autor

Pedro Pessoa Sereno

## Repositório

https://github.com/peropessoa007/controle-gastos 
