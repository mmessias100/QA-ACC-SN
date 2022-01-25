#test1 = input()
#test2 = input()
#test3 = input("Please type in a number:")

# == equals
# != not
# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to


# Boolean logic AND OR NOT
#if test1 == test2 or not(test1 != test3) or test2 == test3:
  #  print("My boolean is outputting true")
#else:
 #   print("My boolean is outputting false")

# Lists in boolean logics
#tree_var1 = input("Type in a tree: ")
#trees = ["Larch","Oak","Pine","Willow"]

#if tree_var1 in trees:
   # print("You have typed a tree that was in my list")
#else:
   # print("FAIL")



# mark = int(input("Enter a number and we'll tell you what your mark is: "))

# if mark >= 85:
#     print("Distinction")
# elif mark >= 65 and mark <= 85:
#     print("Pass")
# elif mark >= 1 and mark <=64:
#     print("Fail")
# else:
#     print("Unknown Error")

# Exercise - Creating a python program that asks a user for an input then grades them based on the number inputtted.

another_mark = int(input("Enter another number and we'll tell you what your mark is: "))
if another_mark <85:
    if another_mark >= 65 and another_mark <85:
        print("Pass")
    else:
        print("Fail")
else:
    print("Distinction")

# Exercise - Odd or Even numbers

# num = int(input("Enter a number: "))  
# if (num % 2) == 0:  
#    print("{0} is Even number".format(num))  
# else:  
#    print("{0} is Odd number".format(num))


# Determining the name of a shape from its number of sides

# tri = 3
# quad = 4
# pent = 5

# name_shape = input("Enter number of sides of a shape: ")
# if name_shape == tri:
#     print("This shape is a triangle")
# elif name_shape == quad:
#     print("This shape is a quadrilateral")
# elif name_shape == pent:
#     print("This shape is a pentagon")


# Leap year challenge

# year = int(input("Enter a year: "))

# if year % 400 == 0 and year % 100 == 0:
#     print("{0} is a leap year".format(year))
# elif year % 4 == 0 and year & 100 != 0:
#     print("{0} is a leap year".format(year))
# else:
#     print("{0} is not a leap year".format(year))