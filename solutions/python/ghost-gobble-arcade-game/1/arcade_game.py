"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verifica se o Pac-Man pode comer um fantasma se ele estiver com uma pílula de poder ativa.

    :param power_pellet_active: bool - o jogador possui uma pílula de poder ativa?
    :param touching_ghost: bool - o jogador está tocando em um fantasma?
    :return: bool - um fantasma pode ser comido?
    """
    return power_pellet_active and touching_ghost
eat_ghost(False, True)


def score(touching_power_pellet, touching_dot):
    """Verifica se o Pac-Man marcou pontos ao comer uma pílula de poder ou um ponto.

    :param touching_power_pellet: bool - o jogador está tocando em uma pílula de poder?
    :param touching_dot: bool - o jogador está tocando em um ponto?
    :return: bool - o jogador marcou pontos ou não?
    """
    return touching_power_pellet or touching_dot
score(True, True)



def lose(power_pellet_active, touching_ghost):
    """Dispara o fim do jogo (GAME OVER) quando o Pac-Man toca em um fantasma sem sua pílula de poder.

    :param power_pellet_active: bool - o jogador possui uma pílula de poder ativa?
    :param touching_ghost: bool - o jogador está tocando em um fantasma?
    :return: bool - o jogador perdeu o jogo?
    """
    return not power_pellet_active and touching_ghost
lose(False, True)


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Dispara o evento de vitória quando todos os pontos foram comidos.

    :param has_eaten_all_dots: bool - o jogador "comeu" todos os pontos?
    :param power_pellet_active: bool - o jogador tem uma pílula de poder ativa?
    :param touching_ghost: bool - o jogador está tocando em um fantasma?
    :return: bool - o jogador ganhou o jogo?
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
win(False, True, False)
