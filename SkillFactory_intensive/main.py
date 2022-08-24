import random as rnd

n = int(input('Enter the length of password --> '))
password = ''


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet += 'ABCDEFJHIJKLMNOPQRSTUVWXYZ'
alphabet += '!@#$%^&*()-_+=;:,./?\|`~[]{}'

choice = input('Wanna use some digits?(y/n)')
if choice == 'y'or choice == 'yes' or choice =='Y' or choice == 'YES':
    alphabet += '1234567890'
elif choice == 'n':
    pass



for item in range(n):
    password += rnd.choice(alphabet)

print(password)

