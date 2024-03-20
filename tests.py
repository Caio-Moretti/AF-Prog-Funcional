import pytest
from main import adicao, operacao, criar_menu, outra_operacao, Monad


def test_adicao():
    assert adicao(2, 3) == 5
    assert adicao(-5, 10) == 5
    assert adicao(0, 0) == 0


def test_operacao():
    assert operacao(lambda x, y: x + y, 2, 3) == 5
    assert operacao(lambda x, y: x - y, 5, 2) == 3
    assert operacao(lambda x, y: x * y, 4, 6) == 24
    assert operacao(lambda x, y: x / y, 8, 4) == 2


def test_criar_menu():
    menu = criar_menu()
    assert len(menu) == 4
    assert menu == ['1: Soma', '2: Subtração', '3: Multiplicação', '4: Divisão']


def test_outra_operacao(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 's')
    assert outra_operacao() is True

    monkeypatch.setattr('builtins.input', lambda _: 'n')
    assert outra_operacao() is False


def test_monad_bind():
    monad = Monad(5)
    monad_result = monad.bind(lambda x: x + 2)
    assert monad_result.get_value() == 7

    monad_error = Monad(None, error="Erro")
    monad_error_result = monad_error.bind(lambda x: x + 2)
    assert monad_error_result.get_value() == "Erro"


def test_monad_invalid_operation():
    monad = Monad(5)
    monad_result = monad.bind(lambda _: "string" + 2)
    assert monad_result.get_value().startswith("Erro")


if __name__ == '__main__':
    pytest.main()
