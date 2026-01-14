"""Funções para prevenir um derretimento nuclear."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verifica se a criticalidade está balanceada.

    :param temperature: int ou float - valor da temperatura em kelvin.
    :param neutrons_emitted: int ou float - número de nêutrons emitidos por segundo.
    :return: bool - a criticalidade está balanceada?

    Diz-se que um reator está com a criticalidade balanceada se ele satisfizer as seguintes condições:
    - A temperatura é menor que 800 K.
    - O número de nêutrons emitidos por segundo é maior que 500.
    - O produto da temperatura pelos nêutrons emitidos por segundo é menor que 500000.
    """
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000
is_criticality_balanced(750,600)


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Avalia a zona de eficiência do reator.

    :param voltage: int ou float - valor da tensão.
    :param current: int ou float - valor da corrente.
    :param theoretical_max_power: int ou float - potência que corresponde a 100% de             eficiência.
    :return: str - uma das opções ('green', 'orange', 'red' ou 'black').

    A eficiência pode ser agrupada em 4 faixas:

    1. green -> eficiência de 80% ou mais,
    2. orange -> eficiência de menos de 80% mas pelo menos 60%,
    3. red -> eficiência abaixo de 60%, mas ainda 30% ou mais,
    4. black -> menos de 30% de eficiência.

    O valor da porcentagem é calculado como (generated_power/theoretical_max_power)*100
    onde generated_power = voltage * current 
    """
    generated_power = voltage * current
    percentual = (generated_power/theoretical_max_power) * 100
    if percentual >= 80:
        return 'green'
    if   60 <= percentual < 80:
        return 'orange'
    if  30 <= percentual < 60:
        return 'red'
    return 'black'
reactor_efficiency(200,50,15000)


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Avalia e retorna o código de status para o reator.

    :param temperature: int ou float - valor da temperatura em kelvin.
    :param neutrons_produced_per_second: int ou float - fluxo de nêutrons.
    :param threshold: int ou float - limite para a categoria.
    :return: str - 'LOW', 'NORMAL', 'DANGER'

    1. 'LOW' -> (temperature * neutrons_produced_per_second) < 90% de threshold
    2. 'NORMAL' -> (temperature * neutrons_produced_per_second) +/- 10% de threshold
    3. 'DANGER' -> (temperature * neutrons_produced_per_second) - não está nas faixas           mencionadas acima
    """
    if (temperature * neutrons_produced_per_second) < (threshold * 0.9):
        return 'LOW'
    elif (0.9 * threshold) <= (temperature * neutrons_produced_per_second) <= (1.1 * threshold):
        return 'NORMAL'
    else:
        return 'DANGER'
