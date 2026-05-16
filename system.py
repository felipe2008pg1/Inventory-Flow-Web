import time
from backend import datos
from backend import tools as to

to.carregar_dados()
to.limpar_tela()

to.escrever_menu("\n📊 GERENCIAMENTO DE ESTOQUE 📊 ", pular_linha=False)
time.sleep(0.4)
to.escrever_menu("- By @dlv.gonzalezz")

while True:

    to.limpar_tela()

    try:
        print(f"\n🕐 | Data: {to.mostrar_hora()}")

        menu = int(input("\n1 - Ver estoque \n2 - Adicionar produto \n3 - Remover item \n4 - Sair \n ESCOLHA: ").strip())
        
        if menu == 1:
            to.mostrar_estoque()
            input("\nPressione ENTER para voltar.")

        elif menu == 2:
            produto = input("Nome do produto: ").strip().upper()
            preco = float(input("Preço: ").strip())
            to.adicionar_estoque(produto, preco)
            time.sleep(1)

        elif menu == 3:
            to.mostrar_estoque() 
            to.remover_do_estoque()
            time.sleep(1)

        elif menu == 4:
            to.encerramento()
            break

        else:
            print("Opção inválida! Escolha entre 1 e 4.")
            time.sleep(2)
            
    except ValueError:
        print("\n[⚠️] ERRO Digite apenas números inteiros para as opções do menu. [⚠️]")
        time.sleep(2)
