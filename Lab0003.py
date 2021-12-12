#!/usr/bin/env python3

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2021"
__credits__ = ["Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Release"

#Ask about Does the program output the correct Truth Values for
#(a) modus ponens and (b) modus tollens in all p -> q combinations?
__editor__ = "Taylor M. Lynch"
___Date___ = "2/4/2021"

from sympy import *

class Proof:
    """A class to demonstrate the modus ponens rule of inference"""

    def Proposition(self, p):
        """Takes in a single proposition as a Boolean value and returns the appropriate Truth Value"""
        return sympify(p)

    def Implication(self, p, q):
        """Takes in two propositions as Boolean values and returns appropriate Truth Value based on the implication connective"""
        x, y = symbols('x, y')

        return (x >> y).subs({x : p, y : q})

    # implement modus ponens starting on the next line
    def ImplementPonens(self, p, q):
        simplify((P & (P >> Q)) >> Q)

        return (Q).subs({P : p, Q : q})
    # implement modus tollens starting on the next line
    def ImplementTollens(self, p, q):
        simplify((Q & (Q >> P)) >> P)

        return (P).subs({P : p, Q : q})
# instantiate a Proof() object

"""# Example of evaluating a single proposition
p = True
q = '~true'
  print(proof.Proposition(p))
   print(proof.Proposition(q))
#Example of evaluating an implication statement
result = proof.Implication(True, True)"""

#Display Fun Fact
print("     Before we get started heres a fun fact!")
print("     Modus ponens is latian for mode that affirms :))")
print(" ")

#Prompt user to input value for p and q
P = input("Enter Boolean input for p (T/F): ")
Q = input("Enter Boolean input for q (T/F): ")
#P, Q = symbols('x, y')

#Prompt the user to pick a a rule of inference
print("Which rule of inference would you like to employ?")
print("If you would like to use Modus Ponens then type 'ponens'")
print("If you would like to use Modus Tollens then type 'tollens'")
print(" ")
input = input("Enter rule of inference: ")
#Use if elif statements to direct the output
if input == 'ponens':
    if P == 'T':
        if Q == 'T':
            P, Q = symbols('P, Q')
            proof = Proof()
            p = True
            q = True
            ponenresult = proof.ImplementPonens(True, True)
            print(ponenresult)
        elif Q == 'F':
            P, Q = symbols('P, Q')
            proof = Proof()
            p = True
            q = '~true'
            ponenresult = proof.ImplementPonens(True, False)
            print(ponenresult)
    elif P == 'F':
        if Q == 'T':
            P, Q = symbols('P, Q')
            proof = Proof()
            p = '~true'
            q = True
            ponenresult = proof.ImplementPonens(False, True)
            print(ponenresult)
        elif Q == 'F':
            P, Q = symbols('P, Q')
            proof = Proof()
            p = '~true'
            q = '~true'
            ponenresult = proof.ImplementPonens(False, False)
            print(ponenresult)

elif input == 'tollens':
    if P == 'T':
        if Q == 'T':
            P, Q = symbols('P, Q')
            proof = Proof()
            p = True
            q = True
            tollenresult = proof.ImplementTollens(True, True)
            print(tollenresult)
        elif Q == 'F':
            P, Q = symbols('P, Q')
            proof = Proof()
            p = True
            q = '~true'
            tollenresult = proof.ImplementTollens(True, False)
            print(tollenresult)
    elif P == 'F':
        if Q == 'T':
            P, Q = symbols('P, Q')
            proof = Proof()
            p = '~true'
            q = True
            tollenresult = proof.ImplementTollens(False, True)
            print(tollenresult)
        elif y == 'F':
            P, Q = symbols('P, Q')
            proof = Proof()
            p = '~true'
            q = '~true'
            tollenresult = proof.ImplementTollens(False, False)
            print(tollenresult)
