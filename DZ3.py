# Напиши функцию возведение в степень, используя цикл for, range и умножение

def degree(namber, degrees):
    for _ in range(degrees - 1):
        namber *= namber
    print(namber)




print(degree(3, 2))
