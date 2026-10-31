# Водоёмы
LAKE = "озеро"
RIVER = "река"
SEA = "море"

# Названия рыб
CARP = "карп"
PIKE = "щука"
PERCH = "окунь"

TROUT = "форель"
GRAYLING = "хариус"
BREAM = "лещ"

COD = "треска"
MACKEREL = "скумбрия"
FLOUNDER = "камбала"


def is_water(water):
    """Проверяет, существует ли такой водоём."""
    return water == LAKE or water == RIVER or water == SEA


def fish_count(water):
    """Возвращает количество видов рыб в выбранном водоёме."""
    if water == LAKE:
        return 3
    elif water == RIVER:
        return 3
    elif water == SEA:
        return 3
    return 0


def fish_by_number(water, number):
    """Возвращает рыбу по номеру для выбранного водоёма."""
    if water == LAKE:
        if number == 1:
            return CARP
        elif number == 2:
            return PIKE
        elif number == 3:
            return PERCH

    elif water == RIVER:
        if number == 1:
            return TROUT
        elif number == 2:
            return GRAYLING
        elif number == 3:
            return BREAM

    elif water == SEA:
        if number == 1:
            return COD
        elif number == 2:
            return MACKEREL
        elif number == 3:
            return FLOUNDER

    return None


def fish_price(fish):
    """Возвращает цену рыбы в монетах."""
    if fish == CARP:
        return 12
    elif fish == PIKE:
        return 18
    elif fish == PERCH:
        return 8

    elif fish == TROUT:
        return 20
    elif fish == GRAYLING:
        return 16
    elif fish == BREAM:
        return 10

    elif fish == COD:
        return 22
    elif fish == MACKEREL:
        return 14
    elif fish == FLOUNDER:
        return 17

    return 0