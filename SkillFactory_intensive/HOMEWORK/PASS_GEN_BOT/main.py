import random as rnd
import string as st
# from ilia_kabakov_first_bot import generator as g


#   создаем класс для генерации
class Password:
    def __init__(self, length: int = 10):
        self.choice1 = 'y'
        self.choice2 = 'y'
        self.spec_symbols: str = "!@#$%^&*()-_+=;:,./?\|`~[]{}"
        self.digits: str = st.digits
        self.alphabet: str = st.ascii_letters
        self.password: str = ''
        self.length: int = length

    def with_digits(self, choice1: str):
        """Метод для добавления цифр к генерации"""
        self.choice1 = str('y')
        if self.choice1 == 'y' or self.choice1 == 'yes' or self.choice1 == 'Y' or self.choice1 == 'YES':
            self.alphabet += self.digits
            return self.alphabet
        elif self.choice1 == 'n' or self.choice1 == 'no' or self.choice1 == 'N' or self.choice1 == 'No':
            return self.alphabet
        else:
            raise ValueError(f"Need to answer Yes or No! Your answer: {self.choice1}")

    def with_special_symbols(self, choice2: str):
        """Метод для добавления символов к генерации"""
        self.choice2 = str('y')
        if choice2 == 'y' or choice2 == 'yes' or choice2 == 'Y' or choice2 == 'YES':
            self.alphabet += self.spec_symbols
            return self.alphabet
        elif choice2 == 'n' or choice2 == 'no' or choice2 == 'N' or choice2 == 'No':
            return self.alphabet
        else:
            raise ValueError(f"Need to answer Yes or No! Your answer: {self.choice2}")

    def check_length(self):
        """Проверка длинны будущего пароля"""
        if 6 <= self.length <= 100:
            return self.length
        else:
            raise ValueError(f'The value can been min 6 and  max 100! Your value: {self.length}')

    def password_gen(self):
        """Собственно сам генератор"""
        for i in range(self.check_length()):
            self.password += rnd.choice(self.alphabet)  # yield?
        return self.password

    def generate(self):
        """Метод вызовов"""
        if self.check_length():
            self.with_digits(self.choice1)
            self.with_special_symbols(self.choice2)
            self.password_gen()
        return self.password


if __name__ == '__main__':
    pg = Password(int(input("Введите желаемое количество символов: \n")))
    print(pg.generate())
