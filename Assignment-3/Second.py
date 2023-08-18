# Q1
#----------------------------------------------------------------

# def print_name_and_age(name, age):
#     print("Name:", name)
#     print("Age:", age)

# # Test the function
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# print_name_and_age(name, age)

#----------------------------------------------------------------
# Q2
#----------------------------------------------------------------

# def show_employee(employeName, salary):
#     print("Name:", employeName)
#     print("Salary:", salary)


# employeName = input("Enter your employeName: ")
# salary = input("Enter your Salary: ")
# if salary == '':
#     salary = 9000

# show_employee(employeName, salary)

#----------------------------------------------------------------
# Q3
#----------------------------------------------------------------

# def create_list(*args):
#     return list(args)

# a = 4
# b = 8
# c = 10
# d = 12

# result_list = create_list(a, b, c, d)
# print(result_list)

#----------------------------------------------------------------
# Q4
#----------------------------------------------------------------

# def km_to_miles(kilometers):
#     miles = kilometers * 0.621371  
#     return miles


# kilometers = float(input("Enter distance in kilometers: "))
# miles = km_to_miles(kilometers)
# print(f"{kilometers} kilometers is equal to {miles} miles")

#----------------------------------------------------------------
# Q5
#----------------------------------------------------------------

# def is_divisible_by_11(number):
#     return number % 11 == 0

# num = int(input("Enter an integer: "))
# if is_divisible_by_11(num):
#     print(f"{num} is divisible by 11")
# else:
#     print(f"{num} is not divisible by 11")

    
#----------------------------------------------------------------
# Q6
#----------------------------------------------------------------

# def get_highest(num1, num2):
#     return max(num1, num2)

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# highest = get_highest(num1, num2)
# print(f"The highest number is: {highest}")

    
#----------------------------------------------------------------
# Q7
#----------------------------------------------------------------

# def fuel_cost(distance, fuel_per_liter=280):
#     cost = (distance / fuel_per_liter) * 100  
#     return cost

# distance = float(input("Enter the distance in kilometers: "))
# fuel_per_liter = float(input("Enter the fuel consumption in liters per 100 kilometers (default is 280): "))

# cost = fuel_cost(distance, fuel_per_liter)
# print(f"The fuel cost for {distance} kilometers is Rs {cost:.2f}")

#----------------------------------------------------------------
# Q8
#----------------------------------------------------------------


def is_valid_email(email):
    if len(email) > 256:
        return False
    
    if email[0].isalpha() or email[0].isdigit():
        pass
    else:
        return False
    
    if "@" in email:
        pass
    else:
        return False
    
    at_index = email.index("@")
    
    if at_index > 0 and at_index < len(email) - 1:
        pass
    else:
        return False
    
    if "." in email[at_index:]:
        pass
    else:
        return False
    
    last_dot_index = email.rindex(".")
    
    if last_dot_index > at_index + 1 and last_dot_index < len(email) - 1:
        return True
    else:
        return False

email = input("Enter an email address: ")
if is_valid_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")








