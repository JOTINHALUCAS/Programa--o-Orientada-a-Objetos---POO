from campus_lista import Gerencia

def menu():
    print("\n===== SISTEMA CAMPUS =====")
    print("1 - Criar Campus")
    print("2 - Listar Campus")
    print("3 - Atualizar Campus")
    print("4 - Criar Curso")
    print("5 - Listar Cursos")
    print("6 - Atualizar Curso")
    print("7 - Excluir Curso")
    print("0 - Sair")

def main():
    sistema = Gerencia()

    while True:
        menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if opcao == 1:
            sistema.criar_campus()

        elif opcao == 2:
            sistema.listar_campus()

        elif opcao == 3:
            sistema.atualizar_campus()

        elif opcao == 4:
            sistema.criar_curso()

        elif opcao == 5:
            sistema.listar_cursos()

        elif opcao == 6:
            sistema.atualizar_curso()

        elif opcao == 7:
            sistema.excluir_curso()

        elif opcao == 0:
            print("Saindo...")
            break
        
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
