# num1=int(input("enter the first number :"))
# num2=int(input("enter the second number :"))
# result=num1/num2
# print(num1)
# print(num1)
# print(result)

# try:
#     num1 = int(input("Enter First Number: "))
#     num2 = int(input("Enter Second Number: "))
#     print(num1)
#     print(num2)

#     result = num1 / num2

#     print(result)
# except ValueError as e:
#     print("Invalid Input Please Input Integer...")
# except ZeroDivisionError as e:
#     print(e)

#A simple example of a lambda function that squares a number:

x=int(input("enter the number:"))
square = lambda x: x**2

# call the lambda function
result = (square(x))

# print the result
print("Result is ",result)
