"""Write a program that finds the sum, product, and arithmetic mean of three integers entered from the keyboard. For example, when entering the numbers 4, 5, and 7, we should get the answer:
4 + 5 + 7 = 16, 4 * 5 * 7 = 140, (4 + 5 + 7) / 3 = 5.333333"""


x = int(input('input first number'))
y = int(input('input second number'))
z = int(input('input third number'))


print(x+y+z)
print(x*y*z)
print((x+y+z)/3)

"""Write a program that raises the input number to the power of 10 using only four multiplication operations."""

number = int(input('Enter number'))
result = number
resultpow2 = result * result
result = resultpow2 * resultpow2
result = result * result
result = result * resultpow2
print(result)
print(number**10)

""" Write a program that takes a three-digit number and 
breaks it down into digits. For example, if you enter 123, 
the program should print: 1, 2, 3 """


number = int(input("input three-digit number: "))
print(number//100, end=" ")
number = number%100
print(number//10, end=" ")
print(number%10, end=" ")


"""universal version for other numbers"""

number = input('input the number: ')
print(f"this is a number {number}")
number_len = len(number)
pow_of_10 = number_len - 1
for i in range(number_len):
    print(int(number) // (10 ** pow_of_10), end=" ")
    number = int(number) % (10** pow_of_10)
    pow_of_10 -= 1