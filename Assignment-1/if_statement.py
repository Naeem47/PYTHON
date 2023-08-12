# Write a program to check whether a person is eligible to vote or not?
# Q.1
# age = 26
# if age >= 18:
#     print('you are eligible to vote')
# else:
#     print('you are not eligible to vote')
#------------------------------------------------

# Write a program to check char is vowel or not.
# Q.2
# value = 'e'
# if value == 'e' or value =='i' or value =='o' or value =='u' or value =='A' or value =='E' or value=='I' or value=='O' or value=='U':
#     print(f"{value} is a Vowel")
# else:
#     print(f"{value} is a constant")
#-----------------------------------------------

# Write a program to check the number is positive or negative. User input.
# Q.3
# userInput = int(input("Please enter a value: "))
# if userInput < 0:
#     print('value is Negative')
# else:
#     print('value is possitive')
#-----------------------------------------------

# Write a program to check whether a number is odd or even?
# Q.4
# userInput = int(input("Please enter a value: "))
# if userInput % 2 == 0:
#     print('this is even number')
# else:
#     print('this is odd number')
#-----------------------------------------------

# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100
# Q.5
# grade = int(input("Enter an integer as input: ")) 
# if grade >= 80:
#     print('Result is A+')
# elif grade < 80 and grade > 69:
#     print('Result is A')
# elif grade < 70 and grade > 59:
#     print('Result is B')
# elif grade < 60 and grade > 49:
#     print('Result is C')
# else:
#     print('Faild')
#-----------------------------------------------

# Write a program to check whether a number is divisible by 7
# Q.6
# userInput = int(input("Please enter a value: "))

# if userInput % 7 == 0  :
#     print('this value is divisible by 7')
# else:
#     print('this value is not divisible by 7')
#-----------------------------------------------

# Write a program to check if year is leap year.
# Q.7
# year = 2000
# if (year % 400 == 0) and (year % 100 == 0):
#     print("is a leap year")
# elif (year % 4 ==0) and (year % 100 != 0):
#     print("is a leap year")
# else:
#     print("is not a leap year")
#-----------------------------------------------

# Write a program to ask user its name and check whether name consists of 5 or more letters
# Q.8
# userInput = input('Please enter ypur name: ')
# if len(userInput)  <= 5:
#     print('letters is between by 5')
# else:
#     print('letters is more then 5')
#-----------------------------------------------

# Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator. Perform operation accordingly
# Q.9
# inputNumber1 = int(input('Please enter a first number: '))
# inputNumber2 = int(input('Please enter a first number: '))
# inputOperation = input('Please enter a mathematical operator: ')
# if inputOperation == '+':
#     print(inputNumber1 + inputNumber2)
# elif inputOperation == '-':
#     print(inputNumber1 - inputNumber2)
# elif inputOperation == '*':15
#     print(inputNumber1 * inputNumber2)
# elif inputOperation == '/':
#     print(inputNumber1 / inputNumber2)
# else:
#     print('please enter a valid number or operator')
#-----------------------------------------------

# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.
# Q.10
# inputNumber = int(input('Please enter a number: '))
# value1 = 2
# value2 = 3
# if inputNumber % 3 == 0 or inputNumber % 2 == 0:
#     if inputNumber % 3 == 0 and inputNumber % 2 == 0:
#      print("divisible by both 2 and 3")
#     elif inputNumber % 3 == 0:
#              print("divisible by 3")
#     elif inputNumber % 2 == 0:
#              print("divisible by 2")
# else: 
#       print("number is not divisible by 2 or 3")
#-----------------------------------------------

# Write a program that accepts 2 inputs from user and check which number is largest.
# Q.11
# inputNumber1 = int(input('Please enter a first number: '))
# inputNumber2 = int(input('Please enter a second number: '))
# if inputNumber1 < inputNumber2:
#     print(f'{inputNumber2} number is larger than {inputNumber1}')
# elif inputNumber1 > inputNumber2:
#     print(f'{inputNumber1} number is larger than {inputNumber2}')
# elif inputNumber1 <= inputNumber2:
#     print('both number are equal')
# else:
#     print('please enter a integar value')
#------------------------------------------------

# Write a program that accepts 3 input from user and check which number is largest.
# Q.12
# inputNumber1 = int(input('Please enter a first number: '))
# inputNumber2 = int(input('Please enter a second number: '))
# inputNumber3 = int(input('Please enter a third number: '))
# if inputNumber1 >= inputNumber2 and inputNumber1 >= inputNumber3:
#     print(f'{inputNumber1} is the largest number ')
# elif inputNumber2 >= inputNumber1 and inputNumber2 >= inputNumber3:
#     print(f'{inputNumber2} is the largest number ')
# elif inputNumber3 >= inputNumber1 and inputNumber3 >= inputNumber2:
#     print(f'{inputNumber3} is the largest number ')
# elif inputNumber3 == inputNumber2 and inputNumber1 == inputNumber3:
#     print('all value are same')
# else:
#     print('please enter a integar value')
#------------------------------------------------

# Write a program that accepts 3 input from user and check the second is largest.
# Q.13
# inputNumber1 = int(input('Please enter a first number: '))
# inputNumber2 = int(input('Please enter a second number: '))
# inputNumber3 = int(input('Please enter a third number: '))
# if inputNumber1 > inputNumber2 and inputNumber1 < inputNumber3:
#     print(f'{inputNumber1} this number is larger then {inputNumber2} and smaller then {inputNumber3} ')
# elif inputNumber1 > inputNumber3 and inputNumber1 < inputNumber2:
#     print(f'{inputNumber1} this number is larger then {inputNumber3} and smaller then {inputNumber2} ')
# elif inputNumber2 > inputNumber1 and inputNumber2 < inputNumber3:
#     print(f'{inputNumber2} this number is larger then {inputNumber1} and smaller then {inputNumber3} ')
# elif inputNumber2 > inputNumber3 and inputNumber2 < inputNumber1:
#     print(f'{inputNumber2} this number is larger then {inputNumber3} and smaller then {inputNumber1} ')
# elif inputNumber3 > inputNumber1 and inputNumber3 < inputNumber2:
#     print(f'{inputNumber3} this number is larger then {inputNumber1} and smaller then {inputNumber2} ')
# elif inputNumber3 > inputNumber2 and inputNumber3 < inputNumber1:
#     print(f'{inputNumber3} this number is larger then {inputNumber2} and smaller then {inputNumber1} ')
# elif inputNumber1 == inputNumber2 and inputNumber1 == inputNumber3:
#     print('All values are equal')
# else:
#     print('please enter a integar value')
#------------------------------------------------

# Write a python program that accept user an input. The valid input should be of following
# Q.14
# colors = ['green', 'red', 'yellow']
# user_input = input("Enter the traffic light color: ")
# input_color = user_input.lower()
# if input_color in colors:
#     if input_color == 'green':
#         print("Car is allowed to go")
#     elif input_color == 'red':
#         print("Car has to stop")
#     else:
#         print("Car has to wait")
# else:
#     print("Invalid input")
#------------------------------------------------

# Write a program to trace your subject mark. Your program should fulfill the following conditions:
# Q.15
# marks = int(input("Enter your subject mark: "))

# if marks < 0 or marks > 100:
#     print("Error: Mark should be between 0 and 100 only")
# elif marks < 50:
#     print("You are fail")
# elif marks >= 50 and marks < 60:
#     print("You are pass")
#     print("Remark: Good")
# elif marks >= 60 and marks < 80:
#     print("You are pass")
#     print("Remark: Very Good")
# else:
#     print("You are pass")
#     print("Remark: Outstanding")
#-------------------------------------------------
