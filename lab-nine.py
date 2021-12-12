__author__ = "Taylor Lynch"
__copyright__ = "Copyright 2021"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "tlynch1@highpoint.edu"
__status__ = "Release"
__desired_grade__ = "A level"
___Purpose____ = "The purpose of this work is to implement a program to compute combinations or permutations."

"""Scenario"""
print("A physician observes a mole on a client's arm. The doctor is concerned")
print("that the mole could be cancerous, but tells the patient to be calm and")
print("that it's probably benign.")
print(" ")
#Of those with skin cancer, 100% have such moles.
ProBgA = float(1) #P(B given Not A)

#However, 20% (0.2) of those without skin cancer also have such moless.
ProBgNotA = float(0.2) #P(B given A)

#If 15% (0.15) of the population has skin cancer.
ProA = float(0.15) #P(A)


#P(A|B) = [P(B|A) * P(A)] / [P(A) * P(B|A) + P(not A)* P(B|not A)
#calculate the probabilty of a person in the population having a mole
ProB = float(ProBgA*ProA + ProBgNotA*(1-ProA))

#Calculate the conditional probability given Bayes' theorem of the
#client having a cancerious mole
ProAgB = float(ProBgA*ProA)/ProB
"""The answer should be 0.46875"""


#Return the conditional probability as a float.
print("what's the probability that this patient has skin cancer?")
print(ProAgB)
