# Ficheiro com a lógica principal do jogo da forca

import random


def escolher_palavra():
    # Lista de palavras disponíveis no jogo
    palavras = ["python", "programacao", "computador", "algoritmo", "terminal"]

    # Escolhe uma palavra aleatória da lista
    return random.choice(palavras)


def mostrar_palavra(palavra, letras_certas):
    # Mostra a palavra com traços nas letras ainda não descobertas
    palavra_mostrada = ""

    for letra in palavra:
        if letra in letras_certas:
            palavra_mostrada += letra + " "
        else:
            palavra_mostrada += "_ "

    return palavra_mostrada


def pedir_letra(letras_usadas):
    # Pede uma letra ao utilizador
    letra = input("Introduz uma letra: ").lower()

    # Verifica se o utilizador introduziu apenas uma letra
    if len(letra) != 1 or not letra.isalpha():
        print("Erro: deves introduzir apenas uma letra.\n")
        return None

    # Verifica se a letra já foi usada
    if letra in letras_usadas:
        print("Essa letra já foi utilizada. Tenta outra.\n")
        return None

    return letra


def verificar_vitoria(palavra, letras_certas):
    # Verifica se todas as letras da palavra já foram descobertas
    for letra in palavra:
        if letra not in letras_certas:
            return False

    return True


def iniciar_jogo():
    palavra = escolher_palavra()
    letras_certas = []
    letras_usadas = []
    tentativas = 6

    print("=== Jogo da Forca ===")
    print("Bem-vindo ao jogo.")
    print("Tenta descobrir a palavra escondida.")
    print("Tens 6 tentativas.\n")

    while tentativas > 0:
        print("Palavra:", mostrar_palavra(palavra, letras_certas))
        print("Tentativas restantes:", tentativas)

        if letras_usadas:
            print("Letras usadas:", ", ".join(letras_usadas))
        else:
            print("Letras usadas: nenhuma")

        letra = pedir_letra(letras_usadas)

        if letra is None:
            continue

        letras_usadas.append(letra)

        if letra in palavra:
            print("Boa! A letra existe na palavra.\n")
            letras_certas.append(letra)
        else:
            print("Errado! A letra não existe na palavra.\n")
            tentativas -= 1

        if verificar_vitoria(palavra, letras_certas):
            print("Parabéns! Conseguiste descobrir a palavra:", palavra)
            break

    if tentativas == 0:
        print("Perdeste! A palavra era:", palavra)