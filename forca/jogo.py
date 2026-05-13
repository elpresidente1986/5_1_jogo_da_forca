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


def iniciar_jogo():
    palavra = escolher_palavra()
    palavra_escondida = mostrar_palavra_escondida(palavra)

    print("=== Jogo da Forca ===")
    print("Bem-vindo ao jogo.")
    print("A palavra foi escolhida automaticamente.")
    print()
    print("Palavra:", palavra_escondida)
    print("Número de letras:", len(palavra))