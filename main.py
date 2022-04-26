while True:
    try:
        n = int(input("Сколько билетов вы хотите приобрести?: "))
    except ValueError:
        print("Ой,это что? А билетов то сколько?")
    print("Укажите возраст каждого посетителя")
    try:
        s = 0
        for i in range(n):
            age = int(input("Возраст посетителя № %d: " %(i+1)))
            if age < 18:
               s += 0
            elif 18 <= age < 25:
               s += 990
            else:
               s += 1390
        if n > 3:
            f = 0.9
        else:
            f = 1
        print("С Вас", s * f, "руб.")
        print("До новых встреч!")
    except ValueError:
        print("Нет, для расчета укажите возраст?")

