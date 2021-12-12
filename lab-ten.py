__author__ = "Taylor Lynch"
__copyright__ = "Copyright 2021"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "tlynch1@highpoint.edu"
__status__ = "Release"
__desired_grade__ = "A level"
__Purpose__ = "The purpose of this work is to develop a program to compute the neighborhood of a given graph and vertex."

#Introduction
print("This program calculates the neighborhood of a given graph and vertex")
print("Be sure not to make repeat entries! You may continue to run this program")
print("after finishing by entering 'y' when prompted to continue.")
print()

#To start the program...
done = False

while done is False:
    print("If you want your input to resemble {(a,b)(a,c)(b,c)}, Then...")
    print("Format your entry set V: ab bc cd de")
    print("Every two letters represents a connected pair of vertices")
    print("and each letter itself is a vertex.")
    print()

    #Prompt user to input the set V as ordered pairs.
    #technically, this is E, FYI). This way we can assume adjacencies and edges.
    v = list(map(str, input("Enter set V: ").split()))
    V = len(v)
    V-=1

    #Prompt user to input a vertex to compute the neighborhood of N(v).
    print("If you want your input to resemble {b,c} ")
    print("Format your entry: bc ")
    vertex = input("Enter a vertex to use in calculating N(v): ")
    print()

    #compute the neighborhood of N(v).
    lst = []
    while V >= 0:
        if vertex in v[V]:
            lst.append(v[V].strip(vertex))
            V -= 1
        else:
            V-=1

    #Output the neighborhood as a set of vertices.
    print("N","(",(vertex),")"," = ", lst)

    #Re-run the program?
    if(input("Would you like to Re-run the program? (y/n): ")  != 'y'):
        done = True
