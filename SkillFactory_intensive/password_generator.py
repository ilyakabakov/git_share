import random as rnd


class Password:
    def __init__(self, length: int = 10):
        self.spec_symbols: str = '!@#$%^&*()-_+=;:,./?\|`~[]{}'
        self.digits: str = '1234567890'
        self.alphabet: str = 'abcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ'
        self.password:str = ''
        self.length = length

    def with_digits(self):
        choice = str(input('Do You want to use some digits?(y/n)\n'))
        if choice == 'y' or choice == 'yes' or choice == 'Y' or choice == 'YES':
            self.alphabet += self.digits
            return self.alphabet
        elif choice == 'n' or choice == 'no' or choice == 'N' or choice == 'No':
            return self.alphabet
        else:
            raise ValueError(f"Need to answer Yes or No! Your answer: {choice}")

    def with_special_symbols(self):
        choice = str(input('Do You want to use some special symbols?(y/n)\n'))
        if choice == 'y' or choice == 'yes' or choice == 'Y' or choice == 'YES':
            self.alphabet += self.spec_symbols
            return self.alphabet
        elif choice == 'n' or choice == 'no' or choice == 'N' or choice == 'No':
            return self.alphabet
        else:
            raise ValueError(f"Need to answer Yes or No! Your answer: {choice}")

    def check_length(self):
        if 6 <= self.length <= 100:
            return self.length
        else:
            raise ValueError(f'The value can been min 6 and  max 100! Your value: {self.length}')

    def password_gen(self):
        for i in range(self.check_length()):
            self.password += rnd.choice(self.alphabet)
        return self.password

    def generate(self):
        if self.check_length():
            self.with_digits()
            self.with_special_symbols()
            self.password_gen()
        return self.password


pg = Password(int(input('Enter length of the password symbols(min:6, max:100):\n')))
print(pg.generate())


