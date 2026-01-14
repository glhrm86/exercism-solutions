"""       
Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: 
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# Definindo a constante EXPECTED_BAKE_TIME       
EXPECTED_BAKE_TIME = 40
# Definindo a constante PREPARATION_TIME 
PREPARATON_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calcula o tempo de forno restante.

    :param elapsed_bake_time: int - tempo de cozimento já decorrido.
    :return: int - tempo de forno restante (em minutos)

    Esta função recebe como argumento os minutos reais que a lasanha esteve no forno e
    retorna quantos minutos a lasanha ainda precisa assar, baseando-se no                       'EXPECTED_BAKE_TIME'.
    """

        
    return EXPECTED_BAKE_TIME - elapsed_bake_time
bake_time_remaining(30)

def preparation_time_in_minutes(numbers_of_layers):
    """Calcula o tempo de preparo dependendo do número de camadas.

    :param number_of_layers: int - número de camadas adicionadas à lasanha
    :return: int - tempo total de preparo (em minutos), onde cada camada leva 2 minutos

    Esta função recebe o número de camadas adicionadas à lasanha e retorna quanto tempo 
    foi gasto no preparo, considerando que cada camada leva 2 minutos para ser adicionada.
    """        
    return PREPARATON_TIME * numbers_of_layers
preparation_time_in_minutes(2)

def elapsed_time_in_minutes(numbers_of_layers, elapsed_bake_time):
    """Calcula o tempo de cozimento decorrido.

    :param number_of_layers: int - o número de camadas da lasanha.
    :param elapsed_bake_time: int - tempo de cozimento decorrido.
    :return: int - tempo total decorrido (em minutos) de preparo e cozimento.

    Esta função recebe dois números inteiros representando o número de camadas da lasanha e     o tempo já gasto assando, e calcula o total de minutos decorridos no cozimento da           lasanha.
    """
    prep_time = preparation_time_in_minutes(numbers_of_layers)
    return prep_time + elapsed_bake_time
elapsed_time_in_minutes(3,20)