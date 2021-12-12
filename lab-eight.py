__author__ = "Taylor Lynch"
__copyright__ = "Copyright 2021"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "tlynch1@highpoint.edu"
__status__ = "Release"
__desired_grade__ = "A level"
___Purpose____ = "The purpose of this work is to implement a program to compute k-permutations."
import math

#Ask the user to input a string
print("You will be prompt one at a time, hit enter when finished.")
print(" ")
print("e.g. string is a string of length six")
string = input("Enter a string: ")
n = string.split()
n = int(len(n))

#Ask the user for k and verify that 0 <= n <= k.
print("The value you enter must be 0 <= k.")
k = input("Enter value: ")
k = int(k)
print(" ")
#if the verification fails...
if k <= 0:
    #ask the user for a larger k.
    print("k must be >= 0.")
    k = input("Enter a larger value: ")
    k = int(k)
elif k > 0:
    k = int(k)
#Rinse and repeat until the verification passes.
print(" ")
#Implement logic such that the program outputs the expected solution given the
# input to n! / (n-k)!
num = math.factorial(n)
temp = n - k
dom = math.factorial(temp)
logic = num / dom
print("n!/(n-k)! =", logic)
#print(logic)
