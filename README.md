# Jogo da Forca

## Definição do problema

Este projeto consiste em criar um jogo da forca em Python.

O objetivo é permitir que o utilizador tente adivinhar uma palavra escondida, introduzindo uma letra de cada vez. A palavra será apresentada com traços e, sempre que o utilizador acertar numa letra, essa letra será mostrada na posição correta.

## Objetivo do jogo

O objetivo do jogo é descobrir a palavra completa antes de terminar o número máximo de tentativas.

## Regras principais

- O utilizador só pode introduzir uma letra de cada vez.
- Se a letra existir na palavra, será apresentada no local correto.
- Se a letra não existir, o utilizador perde uma tentativa.
- Letras repetidas não contam como nova tentativa.
- Não são aceites números, símbolos ou respostas vazias.
- A palavra será escolhida automaticamente pelo programa baseada num conjunto de palavras pré-definidos.

## Vitória e derrota

O jogador ganha se conseguir descobrir a palavra antes de esgotar as tentativas.

O jogador perde se atingir o limite máximo de tentativas sem descobrir a palavra.

## Limitações

- O jogo será feito em Python.
- O jogo será executado no terminal.
- Não terá interface gráfica.
- O número máximo de erros será de 6 tentativas.
- As palavras estarão guardadas numa lista simples dentro do programa.

## Resumo

Criar um programa em Python que permita ao utilizador jogar à forca, tentando descobrir uma palavra escondida através da introdução de letras, respeitando um limite máximo de tentativas.