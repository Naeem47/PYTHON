# # # # input
# # # floor division
# # # x = 10/2
# # # print(x)
# # # print(type(x))

# # # y = 8/2
# # # print(y)
# # # print(type(y))

# # # comparison operator

# # x = 22
# # y=23

# # print(x==y)
# # print(x!=y)
# # print(x>y)
# # print(x<y)
# # print(x>=y)
# # print(x<=y)


# # # # num1 = int(input("enter your number 1 \n "))
# # # # num2 = int( input("enter your Number 2  \n "))
# # # # eng = int( input("enter your Number  \n "))
# # # # math = int( input("enter your Number \n "))
# # # # py = int( input("enter your Number \n "))


# # # # print(f'Math : {math}')
# # # # print(f'Math : {eng}')
# # # # print(f'Math : {py}')
# # # x = 5
# # # y = 10
# # # temp = x
# # # x = y
# # # y = temp

# # # print('The value of x after swapping: {}'.format(x))
# # # print('The value of y after swapping: {}'.format(y))


# # # # print(" FIRST")
# # # # print("A")
# # # # print("B")
# # # # print("C")
# # # # print("SECOND")
# # # # print("A",end="")
# # # # print("B",end="")
# # # # print("C")
# # # # print("LAST")
# # # # print("A","B","C",sep=",")
# # # # print (var)
# # # # String interpolation
# # # # name = "Muhammad-Naeem"
# # # # age = "20"
# # # # print(f"My name is {name} , I am {age} years old")
# # # # print(f"My name is {name}.i am {age} year older then them ")
# # # # print("My name is %s.i am %s year older then them" %(name,age))
# # # # print("My name is {} i am {} year older then them ".format(name,age))


# # # # print ("Math",":", "50",sep="")
# # # # print ("Englis",":"," ", "50",sep='')
# # # # print('There are three "Chickens" in the house')


# # # # name = "M.Naeem"
# # # # profession = "Flutter Developer"
# # # # city  = " Karachi"

# # # # print("My name is",name )
# # # # print("I am a ",profession)
# # # # print("I live in ",city)

# # # # x = 'hello'
# # # # y = ' world '

# # # # print (x+ "" + y)

# # # # z = "world"

# # # # print (f"hello{z}")

# print ("Give marks to see your Grade")

# totalmarks = int( input("Your marks"  ))

# if totalmarks > 90 :
#     print ("Congrats your Grade is A+")
# elif totalmarks < 90 and totalmarks >80 :
#      print ("Congrats your Grade is A")
# elif totalmarks < 80 and totalmarks >70 :
#      print ("Congrats your Grade is B")
# elif totalmarks < 70 and totalmarks >60 :
#      print ("Congrats your Grade is C")
# elif totalmarks < 60 and totalmarks >50 :
#      print ("Congrats your Grade is D")
# elif totalmarks < 50 and totalmarks >35 :
#      print ("Congrats your Grade is E")
# elif totalmarks < 35 and totalmarks >0 :
#      print ("oups youre fail ")

# map object dictionary

# di = {
#     "alia": "hello",
# }
# d2 = {
#     "Hey": "Ola",
# }

# de = di | d2
# de2 = {**di,**de}
# print(de )
# print(de2 )

# d1 = {
#     "name": "M.naeem",
#     "age": "21",
#     "gender": "Male",
# }

# update = {
#     "Salaray": "30K",
#     "Department": "IT",
#     "joining_date": "30-August-2022",   
# }
# d1.update(update)
# print(d1)
# del d1["age"]
# print(d1)
# updated = d1.update({
#     "dob":"26-april=2003"
# })
# print(d1)

# user_friends = [10001,1,55,-8,0,5,-7]

# for id in user_friends :
#     if id == 55:
#         continue
#     if id == 5:
#         break
#     print("friend id",id)


# while loop

# x = 5
# while  x > 5:
#     print(x) 
#     x-=1 #4



# user_input = input("Enter a number between 1 and 10 \n")
# user_input =int(user_input)
# while user_input < 0 or user_input > 10:
#     user_input  = input ("please input a valid number between 1 and 10 \n")
#     user_input = int(user_input)
# print ("valid number is",user_input)


# list = ['0','1','2','3','4','5','6',]


# while len(list)>0:
#     list.pop()
#     print(list)

employe_list = [
    {
        "id" : 1,
        "Name" : "naeem"
    },
    {
        "id" : 2,
        "Name" : "nahid"
    },
    {
        "id" : 3,
        "Name" : "shahid"
    },
    {
        "id" : 4,
        "Name" : "naeem"
    },
    {
        "id" : 5,
        "Name" : "naeem"
    },

   ]
def funct(x):
  for i in employe_list:
    if i["id"] == x:
        # print (employe_list[i])
        value=i

    else:
       continue        
    return value
    
value =  funct(1)
print(value)