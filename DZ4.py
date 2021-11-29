# резюме

class Resume:

    def __init__(self, name, age, fav_prog_land):
        self.name = name
        self.age = age
        self.fav_prog_land = fav_prog_land

    def Print(self):
        print(f"Здраствуйте, меня зовут {self.name}. "
              f"Мне {self.age} года. "
              f"Мой год рождения {2021 - int(self.age)}\n"
              f"Cейчас я изучаю {self.fav_prog_land}")

if __name__ == '__main__':
    my_resume = Resume("Маргарита", "33", "Python")
    my_resume.Print()