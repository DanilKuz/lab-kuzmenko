money = 50
bait = 5
cast_count = 0
last_fish = None
fishes=[]

print("Привет!")

while True:

    command = input("Введите команду:").strip().lower()

    if command == "cast":
        if bait == 0:
            print("Приманка закончилась.")
            continue

        bait -= 1
        cast_count += 1

        if cast_count%3==1:
            last_fish="таранка"
        elif cast_count%3==2:
            last_fish="толстолобик"
        else:
            last_fish="барабулька"

        print(f"Вы поймали: {last_fish}!")

        fishes.append(last_fish)

    elif command == "sell":
        if last_fish is None:
            print("Нет рыбы для продажи.")
            continue
        if last_fish == "таранка":
            price = 10
        elif last_fish == "толстолобик":
            price = 15
        else:
            price = 25
        money += price
        print(f"Вы продали {last_fish} за {price} монет. Баланс: {money}.")
        fishes=fishes[:-1]
        if len(fishes)>=1:
            last_fish = fishes[-1]
        else:
            last_fish=None

    elif command == "status":

        print(f"Деньги: {money} | Приманка: {bait} | Последняя пойманная рыба в наличии: {last_fish} | Рыб в наличии: {len(fishes)}")

    elif command == "exit":
        print("Игра окончена.")
        break

    else:
        print("Неизвестная команда. Введите cast, status, sell или exit.")

