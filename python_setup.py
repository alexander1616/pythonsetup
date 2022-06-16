print("hello from inside a file!")

def hello():
    print("greetings user!")

hello()

def pack(x, y, z):
    return([x, y, z])

print(pack(1, 6, 7))

def eat_lunch(list):
    z = 0
    while z < len(list):
        for i in range(0, len(list)):
            if i == 0:
                print("First I eat " + list[i])
                z += 1
            else:
                print("Next I eat " + list[i])
                z += 1
            
    print("My lunchbox is empty!")

eat_lunch(["soup", "bread", "apple"])


# In class Assignments and Homework Day 2 #

# 1) arb_args - Takes in any number of arguments and prints them one at a time.

def arb_args(*args):
    for i in args:
        print(i)

arb_args(1, 2, 3, 4)

#2) inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.

def inner_func(intA, intB):
    def nest1():
        return intA*intB
    def nest2():
        return intA+intB
    print(nest1() + nest2())

inner_func(5,6)

#3) lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.

def lunch_lady(sname, lunch="Mystery Meat"):
    print(sname, lunch)

lunch_lady("alex", "sandwich")
lunch_lady("mikey")

#4) sum_n_product - Accepts two integers and returns both the sum and the product.

def sum_n_product(x,y):
    return x+y, x*y

#5) alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.

alias_arb_args = arb_args

def alias_arb_args(*args):
    arb_args(args)

#6) arb_mean - Accepts any number of integers and prints their average.

def arb_mean (*args):
    total = 0
    for a in args:
        total += a
        print(a/len(args))

#7) arb_longest_string - Accepts any number of strings and returns the longest one.

def arb_longest_string(*args):
    longestStrCt = len(args[0])
    longestStr = args[0]
    for s in range(1, len(args)):
        if len(args[s]) > longestStrCt:
            longestStrCt = len(args[s])
            longestStr = args[s]
    print(longestStr)
    print(longestStrCt)
    return longestStr




#Homework Practice

# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(intA, intB, intC):
    return max([intA, intB, intC])

# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(lst):
    if len(lst) == 0:
        return 0

    product = lst[0]
    if len(lst) > 1:
        for i in lst[1:]:
            product = product * i
    return product

# Write a Python function called rev_string() to reverse a string.

def rev_string(string):
    return string[::-1]

# Write a Python function called num_within() to check whether a number falls in a given range.
#       The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
#       Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(x, a, b):
    return x in range(a, b+1)

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
#       The function accepts the number n, the number of rows to print
#       Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.


# activity for errors
fileName = input("Please enter the name of the file you would like to read: ")
myfile = open(fileName, 'r') # Open a file for reading.
contents = myfile.readlines() # Read in the content by line.
myfile.close() # Explicitly close the file
print(contents) #print the contents of the file

'''
test code:

f = FileManipulator("tmp.txt")
print(f.contents)
f.reverse("tmp2.txt")
'''

