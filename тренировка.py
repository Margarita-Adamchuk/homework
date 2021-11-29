#Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации
# (отвечающий за добавку к выбираемому лимонаду). В этом классе реализуйте метод show_my_drink(),
# выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки,
# а иначе отобразится следующая фраза: «Обычная газировка».

class Soda:

    def __init__(self, drink):
        if isinstance(drink, str):
            self.drink = drink
        else:
            self.drink = None

    def show_my_drink(self):
        if self.drink:
            print(f"Газировка и {self.drink}")
        else:
            print("Обычная гозировка")

soda = Soda(3)
soda1 = Soda("киви")
soda.show_my_drink()
soda1.show_my_drink()
