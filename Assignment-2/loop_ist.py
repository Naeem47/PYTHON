# 1. Write a Python program to multiply all the items in a list and use for loop. consider the list [3, 5, 2, 1, 4].
# Q.1
# numbersList = [3, 5, 2, 1, 4]
# result = 3
# for i in numbersList:
#     result *= i
# print("Multiplication of all items in the list:", result)
#______________________________________________________________________

# 2. create a list from 0 to 100 using range function and iterate over the list
# Q.2
# myList = []
# for i in range(101):
#     myList.append(i)
#     if i < 100:
#         continue
#     print(myList)
#______________________________________________________________________

# 3. consider the following list ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# Q.3
# myList = ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# for i in myList:
#     if len(i) > 5:
#         print(i)
#______________________________________________________________________

# 4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements using for loop. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] Expected Output : ['Green', 'White', 'Black']
# Q.4
# myList = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] 
# removeItem = [0, 4, 5]
# result_list = []
# for i in range(len(myList)):
#     if i not in removeItem:
#         result_list.append(myList[i])
# print("Expected Output:", result_list)
#______________________________________________________________________

# 5. Write a program to display odd numbers only. odd number upto 100
# Q.5
# for i in range(1,101,2):
#     print(i)
#______________________________________________________________________

# 6. List contains 30 elements. Display first 5 and last 5 elements
# Q.6
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# first_five = my_list[:5]
# last_five = my_list[-5:]
# print("First 5 elements:", first_five)
# print("Last 5 elements:", last_five)
#______________________________________________________________________

# 7. Display output: helloworld from the list [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘w’, ‘o’, ‘r’, ‘l’, ‘d’]
# Q.7
# myList = ['h','e','l','l','o','w','o','r','l','d']
# text = ''
# for i in myList:
#     text += i
#     if len(text) < len(myList):
#         continue
#     print(text)
#______________________________________________________________________

# 8. Write a Python program to append a list to the second list.
# Q.8
# myList = [1, 2, 3, 4, 5]
# updateList = []
# for item in myList:
#     updateList.append(item)
# print("List l2 after appending l1:", updateList)
#______________________________________________________________________

# 9. consider the list ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']
# Q.9
# myList = ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']
# target_word = 'hi'
# count = 0
# for word in myList:
#     if word == target_word:
#         count += 1
# print("The word '{}' appears {} times in the list.".format(target_word, count))
#______________________________________________________________________


