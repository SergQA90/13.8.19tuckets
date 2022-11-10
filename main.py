tuckets = int(input("Укажите количество билетов:"))
sum = 0
for i in range(tuckets):
    age = input("Укажите возраст посетителя:")
    age = int(age)
    if age < 18:
        print("Бесплатный билет")
    elif 25 > age >= 18:
        sum += 990
        print("Цена билета: 990 руб.")
    else:
        sum += 1390
        print("Цена билета: 1390 руб.")
if tuckets > 3:
    sum = sum - ((sum / 100) * 10)
    print(f"Сумма к оплате {sum} руб. с учетом 10%-ой скидки за регистрацию более 3-х человек")
else:
    print(f"Сумма к оплате {sum} руб.")