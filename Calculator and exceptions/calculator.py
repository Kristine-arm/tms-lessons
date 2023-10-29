#Наша задача: сделать приложение "Калькулятор", которое будет запрашивать запрашивать у пользователя два целых числа и операцию (+, -, *, /) и выполняет эту операцию.
#Для завершения программы необходимо будет ввести операцию ! (восклицательный знак).
#Программа должна будет обработать все возможные ошибки, такие как неправильный ввод пользователя.

def input_int_number():
    while True:
        try:
            return int(input('write integer number:   '))
        except ValueError as e:
            print('error raised', e)
            print('write again')

#or the same but with changes

# def input_int_number():
#     while True:
#         try:
#             a = int(input('write number a: '))
#             b = int(input('write number b: '))
#             return a+b
#         except ValueError as e:
#             print ('exception noticed', e)
#
# xyz = input_int_number()
# print(xyz)

class CalculationExitException(Exception):
    pass

#Создайте функцию calculate, которая принимает два целых числа (left и right), и операцию (строку).
#Если строка operation одна их поддерживаемых операций (+, -, *, /) выполните эту операцию. Иначе - выбросьте исключение

def calculate(left: int, right: int, operation: str):
    if operation == '+':
        return left + right
    elif operation == '-':
        return left - right
    elif operation == '*':
        return left * right
    elif operation == '/':
        return left / right
    elif operation =='!':
        raise CalculationExitException()
    else:
        raise ValueError(f'unsupported operation:{operation}')


#Создайте функцию main. Это будет главной функцией вашей программы.
#Функция должна запускать бесконечный цикл, запрашивать у пользователя два числа и операцию, и выводить результат операции (передавая введённые данные в функцию calculate).
#Внутри цикла вам необходимо добавить блок try-except для обработки исключений ValueError (вспомните прошлое задание) и ZeroDivisionError. В случае исключения нужно вывести сообщение об ошибке и продолжить работу.
#Добавьте блок if __name__ == '__main__', в котором будет вызов функции main.


def main():
    while True:
        a = input_int_number()
        b = input_int_number()
        op = input('write operation   ')
        try:
            result = (calculate(a, b, op))
            print(f'result {result}')
        except ValueError as e:
            print ('error', e)
        except ZeroDivisionError as e:
            print ('error', e)
        except CalculationExitException as e:
            print('finish program')
            break

if __name__ == '__main__':
    main()

#Создайте класс CalculationExitException, наследуемый от Exception.
#Внутри функции calculate выбросьте (raise) созданное исключение в случае, если переданная операция это ! (восклицательный знак).
#Обработайте это исключение внутри функции main в дополнительном блоке except. Выведите сообщение "Завершаем программу" и выйдите из бесконечного цикла.


# a = input_int_number()
# b = input_int_number()
# op = input('write operation')
# result = (calculate(a, b, op))
# print(f'result {result}')




