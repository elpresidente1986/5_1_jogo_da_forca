# Ficheiro com a lógica principal do jogo da forca

import random


def escolher_palavra():
    # Lista de palavras disponíveis no jogo
    palavras = ["python", "programacao", "computador", "algoritmo", "terminal"]

    # Escolhe uma palavra aleatória da lista
    return random.choice(palavras)


def mostrar_palavra_escondida(palavra):
    # Mostra a palavra escondida através de traços
    palavra_escondida = "_ " * len(palavra)

    return palavra_escondida


def pedir_letra():
    # Pede uma letra ao utilizador
    letra = input("Introduz uma letra: ").lower()

    # Verifica se o utilizador introduziu apenas uma letra
    if len(letra) != 1 or not letra.isalpha():
        print("Erro: deves introduzir apenas uma letra.")
        return None

    return letra


def iniciar_jogo():
    palavra = escolher_palavra()
    palavra_escondida = mostrar_palavra_escondida(palavra)

    print("=== Jogo da Forca ===")
    print("Bem-vindo ao jogo.")
    print("A palavra foi escolhida automaticamente.")
    print()
    print("Palavra:", palavra_escondida)
    print("Número de letras:", len(palavra))
    print()

    letra = pedir_letra()

    if letra is not None:
        print("Letra introduzida:", letra)