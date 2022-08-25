import random as rnd
import string as st


#   создаем класс для генерации
class Password:
    def __init__(self, length: int = 10):
        self.spec_symbols: str = st.punctuation
        self.digits: str = st.digits
        self.alphabet: str = st.ascii_letters
        self.password: str = ''
        self.length = length

    def with_digits(self):
        """Метод для добавления цифр к генерации"""
        choice = str(input('Do You want to use some digits?(y/n)\n'))
        if choice == 'y' or choice == 'yes' or choice == 'Y' or choice == 'YES':
            self.alphabet += self.digits
            return self.alphabet
        elif choice == 'n' or choice == 'no' or choice == 'N' or choice == 'No':
            return self.alphabet
        else:
            raise ValueError(f"Need to answer Yes or No! Your answer: {choice}")

    def with_special_symbols(self):
        """Метод для добавления символов к генерации"""
        choice = str(input('Do You want to use some special symbols?(y/n)\n'))
        if choice == 'y' or choice == 'yes' or choice == 'Y' or choice == 'YES':
            self.alphabet += self.spec_symbols
            return self.alphabet
        elif choice == 'n' or choice == 'no' or choice == 'N' or choice == 'No':
            return self.alphabet
        else:
            raise ValueError(f"Need to answer Yes or No! Your answer: {choice}")

    def check_length(self):
        """Проверка длинны будущего пароля"""
        if 6 <= self.length <= 100:
            return self.length
        else:
            raise ValueError(f'The value can been min 6 and  max 100! Your value: {self.length}')

    def password_gen(self):
        """Собственно сам генератор"""
        for i in range(self.check_length()):
            self.password += rnd.choice(self.alphabet)  #yield?
        return self.password

    def generate(self):
        """Метод вызовов"""
        if self.check_length():
            self.with_digits()
            self.with_special_symbols()
            self.password_gen()
        return self.password


pg = Password(int(input('Enter length of the password symbols(min:6, max:100):\n')))
print(pg.generate())
