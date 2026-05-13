# Menu do jogo Terminal Zero

import os
import time
import random

largura = 17

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def escrever(texto, velocidade=0.05):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidade)
    print()

def linha():
    print('||' + '=' * largura + '||')

def loading_screen():
    mensagens = []
    for i in range(11):
        limpar_tela()
        print("Carregando Terminal Zero\n")
        if i == 2:
            mensagens.append("Carregando sistema...")
        elif i == 5:
            mensagens.append("Falha na memória detectada")
            time.sleep(0.6)
        elif i == 8:
            mensagens.append("Sinal de vida encontrado")
        elif i == 10:
            mensagens.append("Conectando...")
            time.sleep(1.5)
        for msg in mensagens:
            print(f"> {msg}")
        print()
        barra = "■" * i + "□" * (10 - i)
        print(f"[{barra}]")
        time.sleep(0.4)
    time.sleep(1)

def menu_principal():
    limpar_tela()
    time.sleep(0.8)
    linha()
    print('||  Terminal Zero  ||')
    linha()
    print('||  Status: Online ||')
    print('||  Sinal: Fraco   ||')
    linha()
    print('|| > 1: Novo Jogo  ||')
    print('|| > 2: Sobre      ||')
    print('|| > 3: Sair       ||')
    linha()
    try:
        opcao = int(input('> '))
        return opcao
    except ValueError:
        return 0

def menu_sobre():
    limpar_tela()
    linha()
    print('||  Terminal Zero  ||')
    linha()
    print('||  projeto indie  ||')
    print('||    ASCII/Dos    ||')
    print('|| Feito em Python ||')
    linha()
    print('|| Pressione ENTER ||')
    linha()
    input()

def tela_saida():
    chars = ["#", "@", "%", "&", "?", "0", "1"]
    limpar_tela()
    escrever("ENCERRANDO SISTEMA...", 0.06)
    time.sleep(1)
    escrever("DESCONECTANDO USUÁRIO...", 0.05)
    time.sleep(1.5)
    escrever("FALHA NA MEMÓRIA DETECTADA...", 0.04)
    time.sleep(1)
    escrever("TRANSMISSÃO INSTÁVEL...", 0.05)
    time.sleep(2)
    limpar_tela()
    for i in range(10):
        linha_corrupcao = ""
        for j in range(40):
            linha_corrupcao += random.choice(chars)
        print(linha_corrupcao)
        time.sleep(0.08)
    time.sleep(1)
    limpar_tela()
    escrever("NO SIGNAL", 0.12)
    time.sleep(2)
    limpar_tela()

def opcoes_menu():
    while True:
        opcao = menu_principal()
        if opcao == 1:
            limpar_tela()
            print("JOGO AINDA EM DESENVOLVIMENTO")
            input("\nPressione ENTER...")
        elif opcao == 2:
            menu_sobre()
        elif opcao == 3:
            tela_saida()
            break

def init():
    loading_screen()
    opcoes_menu()
init()