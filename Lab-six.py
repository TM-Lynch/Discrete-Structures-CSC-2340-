__author__ = "Taylor Lynch"
__copyright__ = "Copyright 2021"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "tlynch1@highpoint.edu"
__status__ = "Release"
#Compute whether the input value is composite or prime.
def check_prime(num):
    if num < 2:
        print("Number must be 2 or greater!")
    elif num >= 2:
        factors = [(1, num)]
        i = 2
        while i * i <= num:
            if num % i == 0:
                factors.append((i,num//i))
            i += 1
        if len(factors) > 1:
            print( num, " is a composite number")
        else:
            print(num, " is a prime number")

#explain program to user
print("This program allows you to input a value greater")
print("then 2 and outputs if the number is prime or composite.")
print(" ")

#Ask the user to input a positive integer.
num = input("Enter a positive integer value: ")
num=int(num)

#Output the decision.
check_prime(num)
