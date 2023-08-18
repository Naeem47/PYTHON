# Q1
#-----------------------------------------------------------------------

# li = [1, 2, 3, 4]
# l2 = []

# for i in li:
#     l2.append(i)

# print(l2)

#-----------------------------------------------------------------------

# Q2

#-----------------------------------------------------------------------

# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 3]

# for i in l1:
#         for j in l2:
#             if i == j:
#                 print(" True")
#             else :
#                 (" False")

#-----------------------------------------------------------------------

# Q3

#-----------------------------------------------------------------------

# l = [100, 200, 300, 400]

# for index, value in enumerate(l):
#     print(index, value)

#-----------------------------------------------------------------------

# Q4

#-----------------------------------------------------------------------

# def find_common_values_with_counts(list1, list2):
#     common_values = {}
    
#     for item1 in list1:
#         for item2 in list2:
#             if item1 == item2:
#                 if item1 in common_values:
#                     common_values[item1] += 1
#                 else:
#                     common_values[item1] = 1
    
#     return common_values

# l1 = ['a', 'b', 'c', 'd']
# l2 = ['e', 'b', 'g', 'd', 'f', 'h']

# common_counts = find_common_values_with_counts(l1, l2)
# print(common_counts)

#-----------------------------------------------------------------------

# Q5

#-----------------------------------------------------------------------

# number = 2783
# count = 0

# while number != 0:
#     count += 1
#     number //= 10
   

# print("Total number of digits:", count)


#-----------------------------------------------------------------------

# Q6

#-----------------------------------------------------------------------


# while True:
#     user_input = input("Enter a number to win Lucky draw ")
    
#     if user_input == '0':
#         print("You won the Lucky Draw")
#         break
    
#     print("You've lost :")

# print("The prize is yours : 🎁")

#-----------------------------------------------------------------------

# Q7

#-----------------------------------------------------------------------

# values = []
# count = 0

# while count < 5:
#     user_input = float(input("Enter a number: "))
#     values.append(user_input)
#     count += 1

# sum_of_values = sum(values)

# print("your values:", values)
# print("Sum of all enterd  values:", sum_of_values)


#-----------------------------------------------------------------------

# Q8

#-----------------------------------------------------------------------

# numbers = []
# while True:
#     user_input = float(input("Enter a number or negative number to quit : "))
    
#     if user_input < 0:
#         break
    
#     numbers.append(user_input)

# sum_of_numbers = sum(numbers)

# print(" Your  entered numbers:", numbers)
# print("Sum of entered numbers:", sum_of_numbers)


#-----------------------------------------------------------------------

# Q9

#-----------------------------------------------------------------------



# names = []

# while True:
#     user_Input = input("Enter a name or enter 'END' to quit ! ")
    
#     if user_Input == "END":
#         break
    
#     names.append(user_Input)
#     print("Name:", user_Input)

# print("I am done.")




#-----------------------------------------------------------------------

# Q10

#-----------------------------------------------------------------------


# l1 = [11, 33, 50]
# result = ""

# for num in l1:
#     result += str(num)

# print(result)


#-----------------------------------------------------------------------

# Q11

#-----------------------------------------------------------------------

# d1 = {"id": 1, "name": "Muhammad Naeem", "gender": "Male"}
# d2 = {}

# for key, value in d1.items():
#     d2[key] = value

# print("d2:", d2)



