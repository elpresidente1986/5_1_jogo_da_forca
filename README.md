# Jogo da Forca

## 5.1 Definição do problema

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

## 5.2 Recolha de requisitos

Nesta fase foram definidos os requisitos do jogo da forca. Os requisitos funcionais indicam o que o programa deve fazer. Os requisitos não funcionais indicam como o programa deve funcionar.

## Requisitos funcionais

1. O programa deve escolher automaticamente uma palavra a partir de uma lista pré-definida.

2. O programa deve apresentar a palavra escondida através de traços, sem mostrar as letras no início do jogo.

3. O utilizador deve conseguir introduzir uma letra de cada vez.

4. O programa deve verificar se a letra introduzida existe ou não na palavra escondida.

5. Quando a letra estiver correta, o programa deve mostrar essa letra na posição certa.

6. Quando a letra estiver errada, o programa deve retirar uma tentativa ao jogador e mostrar quantas tentativas ainda restam.

## Requisitos não funcionais

1. O programa deve ser simples e fácil de utilizar.

2. O programa deve apresentar mensagens claras para orientar o utilizador durante o jogo.

3. O programa deve ser executado no terminal, sem necessidade de interface gráfica.

## 5.3 Fluxograma — Jogo da Forca

Nesta fase foi criado o fluxograma do jogo da forca, representando o funcionamento principal do algoritmo antes da programação.

O fluxograma inclui o início do jogo, a escolha da palavra, o ciclo principal, a validação do input, as decisões sobre letras corretas ou erradas, as condições de vitória e derrota, e o fim do jogo.

```mermaid
flowchart TD
    A([Início]) --> B[Escolher palavra aleatória]
    B --> C[Definir tentativas = 6]
    C --> D[Criar palavra escondida com traços]
    D --> E[Mostrar palavra escondida e tentativas restantes]

    E --> F{Ainda há tentativas e a palavra não foi descoberta?}

    F -- Sim --> G[/Pedir uma letra ao utilizador/]
    G --> H{Input é válido?}

    H -- Não --> I[Mostrar mensagem de erro]
    I --> E

    H -- Sim --> J{Letra já foi usada?}

    J -- Sim --> K[Informar que a letra já foi usada]
    K --> E

    J -- Não --> L[Guardar letra usada]
    L --> M{Letra existe na palavra?}

    M -- Sim --> N[Revelar letra na posição correta]
    N --> O{Palavra completa?}

    O -- Sim --> P[Mostrar mensagem de vitória]
    P --> Q([Fim])

    O -- Não --> E

    M -- Não --> R[Retirar uma tentativa]
    R --> S{Tentativas chegaram a zero?}

    S -- Sim --> T[Mostrar mensagem de derrota e palavra correta]
    T --> Q

    S -- Não --> E

    F -- Não --> Q([Fim])

## 5.6 Testes

Nesta fase foram definidos testes para validar o funcionamento do jogo da forca.

O objetivo dos testes é confirmar se o programa responde corretamente a entradas válidas e inválidas, garantindo maior robustez e evitando erros durante a utilização.

## Casos de teste válidos

| Nº | Entrada | Resultado esperado | Resultado obtido |
|---|---|---|---|
| 1 | `a` | O programa aceita a letra e verifica se existe na palavra. | Conforme esperado |
| 2 | `p` | O programa aceita a letra e atualiza a palavra ou as tentativas. | Conforme esperado |
| 3 | `o` | O programa aceita a letra e continua o jogo. | Conforme esperado |
| 4 | `t` | O programa aceita a letra e verifica se está correta. | Conforme esperado |
| 5 | `m` | O programa aceita a letra e mantém o ciclo do jogo. | Conforme esperado |

## Casos de teste inválidos

| Nº | Entrada | Resultado esperado | Resultado obtido |
|---|---|---|---|
| 1 | `1` | O programa deve apresentar erro por não aceitar números. | Conforme esperado |
| 2 | `@` | O programa deve apresentar erro por não aceitar símbolos. | Conforme esperado |
| 3 | `ab` | O programa deve apresentar erro por ter mais de uma letra. | Conforme esperado |
| 4 | campo vazio | O programa deve apresentar erro por não receber uma letra. | Conforme esperado |
| 5 | letra repetida | O programa deve informar que a letra já foi usada. | Conforme esperado |

## Tratamento de erros

Foi implementado tratamento de erros com `try/except` na validação da letra introduzida pelo utilizador.

Desta forma, o programa consegue identificar entradas inválidas, apresentar uma mensagem clara e continuar a execução sem terminar de forma inesperada.