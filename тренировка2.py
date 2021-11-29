#Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
#Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
#С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
#– Ура, можно построить треугольник!;
#– С отрицательными числами ничего не выйдет!;
#– Нужно вводить только числа!;
#– Жаль, но из этого треугольник не сделать.

class Triangle_Checker:

    def __init__(self, nambers):
        self.nambers = nambers

    def is_triangle(self):
        if all(isinstance(namber, (int, float)) for namber in self.nambers):
            if all(namber > 0 for namber in self.nambers):
                if sorted(self.nambers)[0] + sorted(self.nambers)[1] > sorted(self.nambers)[2]:
                    return "Ура, можно построить треугольник!"
                return "Жаль, но из этого треугольник не сделать"
            return "С отрицательными числами ничего не выйдет!"
        return "Нужно вводить только числа!"

a = Triangle_Checker([3, 5, 2])
print(a.is_triangle())
