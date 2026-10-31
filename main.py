import random

from fishing_data import (
    LAKE,
    RIVER,
    SEA,
    is_water,
    fish_count,
    fish_by_number,
    fish_price,
)


# Виды приманок
WORM = "червяк"
LURE = "блесна"
FLY = "мушка"

# Игровое состояние
money = 50
current_water = None
last_fish = None
fish_available_for_sale = False

worm_count = 0
lure_count = 0
fly_count = 0


def add_random_bait():
    """Добавляет одну случайную приманку в запас."""
    global worm_count, lure_count, fly_count

    bait_number = random.randint(1, 3)

    if bait_number == 1:
        worm_count += 1
        print(f"Найдена приманка: {WORM}.")
    elif bait_number == 2:
        lure_count += 1
        print(f"Найдена приманка: {LURE}.")
    else:
        fly_count += 1
        print(f"Найдена приманка: {FLY}.")


def initialize_baits():
    """Выдаёт игроку пять случайных приманок в начале игры."""
    for _ in range(5):
        add_random_bait()


def show_help():
    """Показывает команды и доступные приманки."""
    print("\nКоманды:")
    print("  озеро / река / море — выбрать или сменить водоём")
    print("  ловить — начать рыбалку")
    print("  статус — показать состояние игрока")
    print("  продать — продать последнюю пойманную рыбу")
    print("  помощь — показать команды")
    print("  выход — завершить игру")
    print(f"Приманки: {WORM}, {LURE}, {FLY}")


def status():
    """Показывает монеты, количество приманок и последнюю пойманную рыбу."""
    total_baits = worm_count + lure_count + fly_count

    print("\n--- Статус ---")
    print(f"Монеты: {money}")
    print(f"Приманки: {total_baits}")
    print(f"  {WORM}: {worm_count}")
    print(f"  {LURE}: {lure_count}")
    print(f"  {FLY}: {fly_count}")

    if current_water is None:
        print("Выбранный водоём: нет")
    else:
        print(f"Выбранный водоём: {current_water}")

    if last_fish is None:
        print("Последняя пойманная рыба: нет")
    elif fish_available_for_sale:
        print(f"Последняя пойманная рыба: {last_fish} (можно продать)")
    else:
        print(f"Последняя пойманная рыба: {last_fish} (уже продана)")


def use_bait(bait):
    """Проверяет наличие приманки и расходует одну штуку."""
    global worm_count, lure_count, fly_count

    if bait == WORM and worm_count > 0:
        worm_count -= 1
        return True
    elif bait == LURE and lure_count > 0:
        lure_count -= 1
        return True
    elif bait == FLY and fly_count > 0:
        fly_count -= 1
        return True

    return False


def random_catch():
    """Случайно выбирает рыбу для текущего водоёма."""
    if current_water is None:
        return None

    fish_number = random.randint(1, fish_count(current_water))
    return fish_by_number(current_water, fish_number)


def cast(bait):
    """Расходует приманку и разыгрывает случайное событие."""
    global last_fish, fish_available_for_sale

    if current_water is None:
        print("Сначала выберите водоём: озеро, река или море.")
        return

    bait = bait.strip().lower()

    if bait != WORM and bait != LURE and bait != FLY:
        print(f"Неизвестная приманка. Выберите: {WORM}, {LURE} или {FLY}.")
        return

    if not use_bait(bait):
        print(f"Приманки «{bait}» нет в запасе.")
        return

    print(f"Вы забросили удочку с приманкой «{bait}».")

    event = random.randint(1, 100)

    if event <= 10:
        print("Обрыв лески! Рыба не поймана, приманка потеряна.")
    elif event <= 20:
        print("Поклёвки не было, зато вы нашли приманку!")
        add_random_bait()
    elif event <= 45:
        print("Хороший клёв!")
        last_fish = random_catch()
        fish_available_for_sale = True
        print(f"Вы поймали рыбу: {last_fish}.")
    elif event <= 75:
        last_fish = random_catch()
        fish_available_for_sale = True
        print(f"Вы поймали рыбу: {last_fish}.")
    else:
        print("Сегодня рыба не клюёт.")


def sell(fish, current_money):
    """Продаёт последнюю пойманную рыбу и возвращает обновлённую сумму."""
    global fish_available_for_sale
    if fish is None or not fish_available_for_sale:
        print("Рыбы для продажи нет.")
        return current_money

    price = fish_price(fish)

    if price <= 0:
        print("Не удалось определить цену рыбы.")
        return current_money

    current_money += price
    fish_available_for_sale = False

    print(f"Вы продали рыбу «{fish}» за {price} монет.")
    print(f"Теперь у вас {current_money} монет.")

    return current_money


def main():
    global money, current_water

    # Фиксированное начальное значение для воспроизводимости случайных событий.
    random.seed(42)

    initialize_baits()

    print("Добро пожаловать на рыбалку!")
    print(f"У вас {money} монет и пять случайных приманок.")
    print("Сначала выберите водоём: озеро, река или море.")

    show_help()

    while True:
        command = input("\nВведите команду: ").strip().lower()

        if is_water(command):
            current_water = command
            print(f"Вы выбрали водоём: {current_water}. Теперь можно рыбачить.")

        elif command == "ловить":
            if current_water is None:
                print("Сначала выберите водоём: озеро, река или море.")
                continue

            bait = input(
                f"Какую приманку использовать ({WORM}, {LURE}, {FLY})? "
            )
            cast(bait)

        elif command == "статус":
            status()

        elif command == "продать":
            money = sell(last_fish, money)

        elif command == "помощь":
            show_help()

        elif command == "выход":
            print("Игра завершена.")
            break

        else:
            print("Неизвестная команда. Введите «помощь», чтобы увидеть команды.")


if __name__ == "__main__":
    main()


