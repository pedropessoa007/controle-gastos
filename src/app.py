import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from app import main

if __name__ == "__main__":
    main()
    
from gastos import adicionar_gasto, listar_gastos, remover_gasto, total_gastos
from cambio import converter_para_dolar

def exibir_menu():
    print("\n===== Controle de Gastos =====")
    print("1. Adicionar gasto")
    print("2. Listar gastos")
    print("3. Remover gasto")
    print("4. Ver total")
    print("5. Ver total em dólar")
    print("0. Sair")
    print("==============================")


def main():
    print("Bem-vindo ao Controle de Gastos Pessoais!")
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            descricao = input("Descrição: ")
            try:
                valor = float(input("Valor (R$): "))
                gasto = adicionar_gasto(descricao, valor)
                desc = gasto['descricao']
                val = gasto['valor']
                print(f"Gasto '{desc}' de R${val:.2f} adicionado.")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            gastos = listar_gastos()
            if not gastos:
                print("Nenhum gasto registrado.")
            else:
                print("\n--- Seus gastos ---")
                for i, g in enumerate(gastos):
                    print(f"[{i}] {g['descricao']} - R${g['valor']:.2f}")

        elif opcao == "3":
            gastos = listar_gastos()
            if not gastos:
                print("Nenhum gasto para remover.")
            else:
                for i, g in enumerate(gastos):
                    print(f"[{i}] {g['descricao']} - R${g['valor']:.2f}")
                try:
                    indice = int(input("Número do gasto para remover: "))
                    removido = remover_gasto(indice)
                    print(f"✔ Gasto '{removido['descricao']}' removido.")
                except (ValueError, IndexError) as e:
                    print(f"✘ Erro: {e}")

        elif opcao == "4":
            total = total_gastos()
            print(f"\nTotal de gastos: R${total:.2f}")

        elif opcao == "4":
            total = total_gastos()
            print(f"\nTotal de gastos: R${total:.2f}")

        elif opcao == "5":
            total = total_gastos()
            if total == 0:
                print("Nenhum gasto registrado.")
            else:
                try:
                    total_usd = converter_para_dolar(total)
                    print(f"\nTotal em dólar: US${total_usd:.2f}")
                except Exception as e:
                    print(f"Erro ao buscar cotação: {e}")

        elif opcao == "0":
            print("Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
