from gastos import adicionar_gasto, listar_gastos, remover_gasto, total_gastos


def exibir_menu():
    print("\n===== Controle de Gastos =====")
    print("1. Adicionar gasto")
    print("2. Listar gastos")
    print("3. Remover gasto")
    print("4. Ver total")
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

        elif opcao == "0":
            print("Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
