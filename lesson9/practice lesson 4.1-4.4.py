#Создайте класс User с публичным поле login и приватным полем __password. Оба поля должны заполняться в конструкторе.
class User:
    def __init__(self, login, password):
        self.login = login
        self.__password = password

#Добавьте метод check_password, который принимает строку с паролем (возможно неправильным), и возвращает
#True, если пароль верный
#False, если пароль неверный
    def check_password(self, password):
        return self.__password == password
        #or we could write if self.__password == password:
        #return true
        #esle: return false

#Добавьте метод reset_password, который принимает строку с новым паролем и обновляет поле __password новым значением.
    def reset_password(self, new_password):
        self.__password == new_password

my_user = User('Kristine', 'SuperSecretP@ssword')

print(my_user.login)
# print(my_user.__password)  # так нельзя, будет ошибка

print(my_user.check_password('WrongPassword'))
print(my_user.check_password('SuperSecretP@ssword'))

my_user.reset_password('NewP@ssword')

print(my_user.check_password('SuperSecretP@ssword'))
print(my_user.check_password('NewP@ssword'))


