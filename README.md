# Atividade Final - Programação Funcional

**Integrantes**:
- Lucas Gomes Andrade: 2116273
- Caio Moretti de Macedo: 2213905
- Leonardo Alex Evaristo Chacon: 2213835
- Gisele Da Costa Soares: 2213825
- Lucas Aguiar Marques: 2124701

> **Tests Code Coverage**:
> ![img.png](img/img.png)

## Projeto: Calculadora com tratamento de erros e testes unitários

Este projeto consiste em uma calculadora simples implementada em Python, que oferece as operações básicas de adição, subtração, multiplicação e divisão. Além disso, a calculadora possui tratamento de erros para garantir que apenas números sejam utilizados nas operações. O projeto também inclui testes unitários para verificar o funcionamento correto das funções.

## Funcionalidades principais:
Calculadora: A função calculadora() permite ao usuário escolher uma operação (soma, subtração, multiplicação ou divisão) e realizar o cálculo com dois números digitados pelo usuário.

Menu: A função criar_menu() cria um menu com as opções de operações disponíveis para o usuário.

Tratamento de erros: O código inclui o uso de uma classe Monad para tratar erros e resultados de cálculos. Caso haja um erro durante o cálculo, a calculadora exibirá uma mensagem de erro.

Testes unitários: O projeto possui testes unitários para as operações de adição, subtração, multiplicação, divisão, criação do menu e verificação se o usuário deseja realizar outra operação.

Como executar:
Para executar a calculadora, basta rodar o script Python main.py. Ao ser executado, o usuário poderá escolher uma operação e inserir dois números para o cálculo. O resultado será exibido na tela.

Como executar os testes:
Os testes unitários estão localizados no arquivo test_main.py. Para executar os testes, basta rodar o comando pytest no terminal na mesma pasta onde os arquivos estão localizados. Os testes verificarão o funcionamento correto das funções da calculadora e seu tratamento de erros.

Dependências:
O projeto utiliza a biblioteca pytest para a execução dos testes unitários. Certifique-se de tê-la instalada antes de executar os testes. Você pode instalar o pytest utilizando o comando pip install pytest.

Esse README.md fornece uma visão geral do projeto e explica como executar a calculadora e os testes unitários. Certifique-se de seguir as instruções para uma experiência tranquila com o projeto da calculadora em Python.
