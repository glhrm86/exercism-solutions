"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """Estimar valor após a troca

    :param budget: float - quantia de dinheiro que planeja trocar.
    :param exchange_rate: float - valor unitário da moeda estrangeira.
    :return: float - valor trocado da moeda estrangeira que pode receber.
    """
    return budget / exchange_rate
exchange_money(127.5, 1.2)

def get_change(budget, exchanging_value):
    """Calcular dinheiro restante após uma troca

    :param budget: float - quantia de dinheiro que possui.
    :param exchanging_value: float - quantia do dinheiro que deseja trocar no momento.
    :return: float - quantia restante da dinheiro inicial após a troca.
    """
    return budget - exchanging_value
get_change(127.5, 120)
    
def get_value_of_bills(denomination, number_of_bills):
    """Calcular valor das cédulas

    :param denomination: int - o valor de uma cédula.
    :param number_of_bills: int - número total de cédulas.
    :return: int - valor calculado das cédulas.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """Calcular número de cédulas que irá receber

    :param amount: float - o valor inicial total.
    :param denomination: int - o valor de uma única cédula.
    :return: int - número de cédulas que podem ser obtidas a partir da quantia.
    """
    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    """Calcular restante após trocar por cédulas

    :param amount: float - o valor inicial total.
    :param denomination: int - o valor de uma única cédula.
    :return: float - a quantia que sobra, dada a denominação atual.
    """
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calcular valor final após câmbio

    :param budget: float - a quantia de dinheiro que planeja trocar.
    :param exchange_rate: float - o valor unitário da moeda estrangeira.
    :param spread: int - porcentagem cobrada como taxa de câmbio.
    :param denomination: int - o valor de uma única cédula.
    :return: int - valor máximo que pode receber.
    """
    taxa_real = exchange_rate * (1 + spread /100)
    total = budget / taxa_real
    cedulas = total // denomination
    return cedulas * denomination
