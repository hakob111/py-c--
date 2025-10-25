name = 'Hakob'
print('Hello', name)

name = input('What is your name?')
print('Hello', name, '!')

num1 = 12
num2 = 15
print(num1 + num2)

num1 = input()
num2 = input()
print(num1 +num2)

num1, num2 = map(int, input("enter 2 digits separated by a space\n"). split(" "))
sum = num1 + num2
print(num1, '+', num2, '=', sum, sep='')