# # input function
# print("What is your name?")
# name = input()
 
# print("How old are you?")
# age = int(input())

# print(name)
# print(age)

# # sys module
# import sys 
# # passed one argument


# print("How old are you?")
# age = int(input())

# print(name)
# print(age)

# # pass  arguments
# import sys

# name = sys.argv[1]
# age = sys.argv[2]

# print(name)
# print(age)


# control flow
# if statement

# height = 74
# if height > 70:
#   print ("You are really tall!")

# if else statememnts

# height = 84
# if height >70:
#     print ("You are really tall!")
# else:
#     print("You are really short!")

# elif statements helps check multiple conditions

# height = 40
# if height > 70:
#     print("You are really tall!")
# elif height > 60:
#     print("You are avarage height!")

# else :
#     print("You are really short!")

# checking for nothing
# name = ""
# list_a= []
 
# if list_a :
#     print("I will not run")
# else:
#     print("I am Empty")

# looping
# using 1. while & 2. for

# for loops
# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number)

# # range in for loop
# list_a = list(range(0,5))
# print(list_a)

# # range has two parameters
# # 1. starts range and stops range

# for i in range(0,7):
#     print("I would love" + str(i) + "cookies")
# # str(i) is used
#  to convet i(which is a number) to strings

# # intro oduls and maths operation

# numbers =[ 1, 2, 3, 4, 5]
# for i in numbers:
#     if i % 2 == 0:
#         print (i)


# while loops
# players = 11

# while players >= 5:
#     print ("The remaining players are", players)
#     players -= 1

# break statements
# number = 0 
# while True:
#     print("I love candy" + str(number))
#     number +=1
#     if number == 7:
#       break


# continue statement
# helps jump to top of loop


# in a team of members 20, some numbers are taken 
# and want to display the numbers that are not taken
# so others don't pick the picked numbers


# # taken numbers
# numTaken = [3,5,7,11,13]

# print("Available numbers")

# # loop
# for i in range(1,21):
#     if i in numTaken:
#         continue
#     print(i)

# break statements
number = 0
while True:
    print("Ilove you " + str(number))
    number +=1
    if number ==7 :
        break