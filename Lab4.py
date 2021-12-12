# Taylor Lynch
# 2/12/2021
#*Hint: set cardinality can help determine if a function type is
#valid given the set inputs. Think about it.
import random
import string
One=[]
Two=[]

print("While entering your sets,inputs may be integer or characters, But they")
print("must be entered with a space inbetween each element in the set.")
print("Ex. of acceptable input: 1 2 3 or a b c ")
print(" ")

while True:
#Ask the user to select the function from a menu of: (1) One-to-One (2) Onto
    NumofSets = input("Enter number of sets you want(1/2): ")
    print("Function options: (1) One-to-One (2) Onto")
    function = input("Enter your secection: ")
    if NumofSets == "1":
        #Prompt user to enter set
        One = input("Enter each element of your set: ")
        if function == "1":
            Two = string.ascii_letters
            random_letters = random.choice(Two)
            one = One.split()
            LOne=len(One.split())
            for i in range(LOne):
                print("f:", one[i], "->", random.choice(Two))
        elif function == "2":
            Two = string.ascii_letters
            random_letters = random.choice(Two)
            one = One.split()
            LOne=len(One.split())
            for i in range(LOne):
                print("f:", one[i], "->", random.choice(Two))
            print("f:", one[LOne-i], "->", random_letters)

    elif NumofSets == "2":
        #Prompt user to enter first set
        One = input("Enter each element of your first set: ")
        #Prompt user to enter second set
        Two = input("Enter each element of your second set: ")
        if function == "1":
            #print("hello")
            one = One.split()
            LOne = len(One.split())
            two = Two.split()
            LTwo = len(Two.split())
#Compute a valid set of element assignments for the selected function.
            if LOne >= LTwo:
                for i in range(LTwo):
                    print("f:", one[i], "->", two[i])
            elif LTwo > LOne:
                for i in range(LOne):
                    print("f:", one[i], "->", two[i])
        elif function == "2":
            one = One.split()
            LOne = len(One.split())
            two = Two.split()
            LTwo = len(Two.split())
#Compute a valid set of element assignments for the selected function.
            if LOne >= LTwo:
                for i in range(LTwo):
                    print("f:", one[i], "->", two[i])
                print("f:", one[LOne-i], "->", two[LTwo-2])
            elif LTwo > LOne:
                for i in range(LOne):
                    print("f:", one[i], "->", two[i])
                print("f:", one[LOne-i], "->", two[LTwo-2])
#Ask the user if they would like to enter another set or quit.
    exit=input("Would you like to try again?(y/n): ")
    if exit=='n':
         print("Bye")
         break
