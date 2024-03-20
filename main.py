# Função principal da calculadora
def calculadora():
    while True:
        menu = criar_menu()
        print("Escolha a operação:")
        for opcao in menu:
            print(opcao)
        opcao = int(input())

        if opcao not in range(len(menu)):
            print("Opção inválida!")
            continue

        operacoes = [adicao, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
        operacao_selecionada = operacoes[opcao]

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado_monad = Monad((num1, num2)).bind(lambda nums: operacao(operacao_selecionada, nums[0], nums[1]))

        imprimir_resultado(resultado_monad.get_value())

        if not outra_operacao():
            break


# List comprehension para criar menu
def criar_menu():
    return [f"{i+1}: {op}" for i, op in enumerate(["Soma", "Subtração", "Multiplicação", "Divisão"])]


# Função para perguntar se deseja fazer outra operação
def outra_operacao():
    resposta = input("Deseja fazer outra operação? (s/n): ")
    return resposta.lower() == 's'


# Closure para armazenar a última operação realizada
def operacao_anterior():
    ultima_operacao = None

    def salvar_operacao(op):
        nonlocal ultima_operacao
        ultima_operacao = op

    def obter_operacao():
        return ultima_operacao

    return salvar_operacao, obter_operacao


# Função de alta ordem para aplicar uma operação a dois números
def operacao(op, a, b):
    return op(a, b)


# Função lambda para adição
adicao = lambda x, y: x + y


# Função de continuação para imprimir o resultado
def imprimir_resultado(resultado):
    print("O resultado é:", resultado)


# Monad para tratar erros e resultados de cálculos
class Monad:
    def __init__(self, valor, error=None):
        self.valor = valor
        self.error = error

    def bind(self, func):
        try:
            novo_valor = func(self.valor)
            return Monad(novo_valor)
        except Exception as e:
            return Monad(None, error="Erro")

    def get_value(self):
        if self.error:
            return self.error
        return self.valor



if __name__ == '__main__':
    calculadora()
