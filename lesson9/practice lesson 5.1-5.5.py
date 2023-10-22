#Давайте теперь хранить пароль в зашифрованном виде. Создайте новое поле __key = random.randint(1, 1000)
import random
class User:
    def __init__(self, login, password):
        self.login = login
        self.__key = random.randint(1, 1000)
        self.__encoded_password = self.__encode(password)
    def check_password(self, password):
        return self.__encoded_password == self.__encode(password)

    def reset_password(self, new_password):
        self.__encoded_password == self.__encode(new_password)

#Добавьте приватный метод __encode, шифрующий строку:
#def __encode(self, s):
#return ''.join([chr(ord(i) ^ self.__key) for i in s])

    def __encode(self, s):
        return ''.join([chr(ord(i) ^ self.__key) for i in s])

my_user = User('Kristine', 'SuperSecretP@ssword')

print(my_user.login)
# print(my_user.__password)  # так нельзя, будет ошибка

print(my_user.check_password('WrongPassword'))
print(my_user.check_password('SuperSecretP@ssword'))

my_user.reset_password('NewP@ssword')

print(my_user.check_password('SuperSecretP@ssword'))
print(my_user.check_password('NewP@ssword'))