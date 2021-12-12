__author__ = "Taylor Lynch"
__copyright__ = "Copyright 2021"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "tlynch1@highpoint.edu"
__status__ = "Release"
__desired_grade__ = "A level"

#Ask the user whether order of output values matters.
order = input("Do you want output to be in order(y/n): ")

#If order does not matter, implement logic such that the program:
if order == 'n':
    set_of_inputs=[]
    sum_rule= 0
    product_rule=1

    set_of_inputs = input("How many sets of inputs will you use: ")
#takes two (C level) set of inputs
    if set_of_inputs == '2':
        print("Enter a set of inputs seperated by spaces.")
        print("When finished entering set, hit enter.")
        print("Then it will allow you to enter your second set.")
        print("")
        set1 = input("Enter first: ")
        set1 = set1.split()
        set2 = input("Enter second: ")
        set2 = set2.split()
        sum_rule = len(set1) + len(set2)
        product_rule = len(set1) * len(set2)
        print("")

#outputs the solution using the sum rule and the product rule (each labeled as such).
        print("Solutions:")
        print("sum rule = ", sum_rule)
        print("product rule = ", product_rule)


#three (B level) set of inputs
    elif set_of_inputs == '3':

        print("Enter a set of inputs seperated by spaces.")
        print("When finished entering set, hit enter.")
        print("Then it will allow you to enter your next set.")
        print("")
        set1 = input("Enter first: ")
        set1 = set1.split()
        set2 = input("Enter second: ")
        set2 = set2.split()
        set3 = input("Enter third: ")
        set3 = set3.split()
        sum_rule = len(set1) + len(set2)
        product_rule = len(set1) * len(set2)
        print("")

#outputs the solution using the sum rule and the product rule (each labeled as such).
        print("Solutions:")
        print("sum rule = ", sum_rule)
        print("product rule = ", product_rule)


#more than 3 (A level) sets of inputs
    else:
        print("Enter a set of inputs seperated by spaces.")
        print("When finished entering set, hit enter.")
        print("Then it will allow you to enter your next set.")
        print("")
        set = [""]
        set = input("Enter set: ")
        while(len(set)>0):
            set = input("Enter set: ")
            set = set.split()
            sum_rule += len(set)
            if (len(set)>0):
                product_rule *= len(set)
        print("")
#outputs the solution using the sum rule and the product rule (each labeled as such).
        print("Solutions:")
        print("sum rule = ", sum_rule)
        print("product rule = ", product_rule)

#If order does matter, implement logic such that the program:
elif order == 'y':
    print("Enter a set of inputs seperated by spaces.")
    print("When finished entering set, hit enter.")
    print("Then it will allow you to enter your subset size.")
    print("Remember your subset size can be zero!")
    print("")
    set = []
#takes one set of inputs
    set = input("Enter set: ")
    set = set.split()
    set_size = len(set)
    #print(set_size)
#a second value (which can be zero!) as the size of the subset
    size_of_subset = int(input("Enter size of subset: "))
    #print(size_of_subset)
    n_r = set_size - size_of_subset
    i = 1
    factorial_n = 1
    factorial_nr = 1
    while i <= n_r:
        factorial_nr = factorial_nr * i
        i = i + 1
    i = 1
    while i <= set_size:
        factorial_n = factorial_n * i
        i = i + 1
    #print(factorial_n,factorial_nr)
    Pnr = factorial_n / factorial_nr
#outputs the solution of P(n, r) (B,A levels) depending on the second value in 3a.
    print("P(n,r) = ", Pnr)
