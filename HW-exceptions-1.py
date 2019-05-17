user_input = input('Введите выражение с помощью польской нотации: ')
input_list = user_input.split()
num1, operation, num2 = input_list[1], input_list[0], input_list[2]
expressions_list = ['+', '-', '*', '/']
expression = num1 + operation + num2

assert operation in expressions_list, 'Такая операция недоступна'

try:
    eval(expression)
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except IndexError:
    print('Вы ввели недостаточное количество данных')
except NameError:
    print('Вы пытаетесь совершить арифметическую операцию со строками - так делать нельзя!')
except SyntaxError:
    print('Вы ввели какие-то несовместимые символы вместо или вместе с числами')
else:
    print(eval(expression))
finally:
    print('Конец операции')
