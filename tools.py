import os
from datetime import datetime
import datos as da
import time
import json

def salvar_dados():
    try:
        with open(da.ARQUIVO, "w", encoding="utf-8") as f:
            # Salvamos a lista que está lá no datos.py
            json.dump(da.estoque, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar: {e}")

def carregar_dados():
    if os.path.exists(da.ARQUIVO):
        try:
            with open(da.ARQUIVO, "r", encoding="utf-8") as f:
                # Atualizamos a lista no datos.py com o que está no arquivo
                da.estoque = json.load(f)
        except Exception as e:
            print(f"Erro ao carregar: {e}")

def mostrar_estoque():
    if len(da.estoque) == 0:
        escrever_lento("O estoque está vázio!")
        print('='*10)
        input("Digite ENTER para voltar: ").strip()
    else:
        for i, t in enumerate(da.estoque,start=1):
            print(f"{i} - {t['produto']:<14} | R${t['preco']}")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else "clear")

def mostrar_hora():
    agora = datetime.now()
    br = agora.strftime("%d/%m/%Y - %H:%M:%S")
    return br

def adicionar_estoque(produto, preco):
    da.estoque.append({'produto': produto, 'preco': preco})
    print(f"Produto {produto} adicionado com sucesso!")
    salvar_dados()

def remover_do_estoque():
        if len(da.estoque) == 0:
            escrever_lento("O estoque está vázio!")
            print('\n='*10)
        else:
            for c, i in enumerate(da.estoque,start=1):
                print(f"{c} - {i['produto']} | {i['preco']}")
            remover = int(input("Digite o índice do produto: ")) - 1
            removido = da.estoque[remover]['produto']
            da.estoque.pop(remover)
            escrever_lento(f"Produto {removido} removido com sucesso.")
            salvar_dados()

def escrever_menu(texto, pular_linha=True):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(0.05)
    
    if pular_linha:
        print()

def escrever_lento(a):
    for letra in a:
        print(letra, end='', flush=True)
        time.sleep(0.05)
    print()

def encerramento():
    print("="*12)
    escrever_lento(">> ENCERRANDO <<")
    print("="*12)

def verificar_adm():

    tentativas = 0

    while True:
        try:
            name_adm = input("Digite seu user adm: ").strip().upper()
            senha_adm = int(input("").strip())
            encontrado = False

            for p in da.dados_autorizados:
                if name_adm == p['adm'] and senha_adm == p['senha']:
                    encontrado = True
                    print('Administrador encontrado.')
                    escrever_lento("CARREGANDO...")
                    time.sleep(1)

            if not encontrado:
                tentativas += 1 
                print("Administrador não encontrado ou dados incorretos")
                escrever_lento(f"Tentativa {tentativas}/3.")
                print("- Reiniciando.. -")
                time.sleep(0.3)
                limpar_tela()

        except ValueError:
            print("Digite números quanto solicitado")
            continue

    
