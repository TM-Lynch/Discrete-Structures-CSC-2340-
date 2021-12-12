#Taylor Lynch 1/27/2021
#I believe this code is an A because Completing requirements 1 through 4
#for ternary quantification will earn a maximum of a A grade
#*how to use the program*
v=[]
equation=['True','False']
#dom_int = list(map(int, dom))
quant=[]
print("  ")
print("In this program you will be entering several quantifier for unary,")
print("binary, and ternary predicates. The program will read the information,")
print("then determin/output if what you  input is true(T) or false(F).")
print("  ")
print("When entering input you need to make sure to have a space")
print("betweeen every element entered or the program will not work.")
print(" ")
print("An example of acceptable input will be displayed before every entry.")
print("Please pay close attention to the examples!")
print(" ")
print(" ")
#valid input for a variable
print("Unary Ex. x ")
print("Binary Ex. x y ")
print("Ternary Ex. x y z ")
#make a loop to make an int
vars = input('Enter variabel for predicate statement: ')
#print(vars)
#if statement to determine if unary, binary or ternary dependent on length
varsL = len(vars)
#print(varsL)
if varsL== 1:
    print(" ")
    print("Unary Ex. x > 0")
elif varsL== 3:
    v=vars.split()
    #print(v)
    print(" ")
    print("Binary Ex. x + y = 0")
elif varsL== 5:
    v=vars.split()
    #print(v)
    print(" ")
    print("Ternary Ex. x / y = z")
#output function example depend ing on number of variables?
#print(" ")
#valid input for a function
print("These are the only options for connectors: > + - / * ")
print("Only enter one connector for function!")
funt= input("Enter function: ")
print(" ")
#print(funt)
#valid input for a domain
#domain is in the form of {n...n+1}
print("Domain Ex. ( 1 2 3 4 5 ) ")
domain = input("Enter domain: ")
dom = domain.split()
dom_object = map(int, dom)
d = list(dom_object)
#print(domain)
#print(dom)
#print(dom_object)
print(d)
#dom=domain.split()

print(" ")
#valid input for quantifiers
print("Ex. u (for Universal) ")
print("Ex. e (for Existential) ")
quant= input("Enter quantifiers: ")
#print(quant)
#print(v[0])
#print(v[1])
#loop variables
i=0
s = i + 1
t = s + 1
#output for Unary
if varsL==1:
    if funt == '>':
        if quant == 'e':
          for i in range(0,len(d)):
              if d[i]>0:
                  print("(" + quant + ")" + vars + funt + "0")
                  print(equation[0])
                  break
              elif d[i]<0:
                  print("(" + quant + ")" + vars + funt + "0")
                  print(equation[1])
                  break
        elif quant == 'u':
            for i in range(0,len(d)):
                if d[i]>0:
                     print("(" + quant + ")" + vars + funt + "0")
                     print(equation[0])
                     break
                elif d[i]<0:
                     print("(" + quant + ")" + vars + funt + "0")
                     print(equation[1])
                     break
#ouptput of a binomial
elif varsL==3:
    if quant == 'e':
    #exostential binomial addition
         if funt == '+':
             for i in range(0,len(d)):
                 if d[i] + d[i] != 0:
                         if d[i] + d[s] != 0:
                             print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                             print(equation[1])
                             break
                 else:
                     print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                     print(equation[0])
                     break
    #exostential binomial subtraction
         elif funt == '-':
             for i in range(0,len(d)):
                 if d[i] - d[i] != 0:
                     if d[i] - d[s] != 0:
                         print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                         print(equation[1])
                         break
                 else:
                     print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                     print(equation[0])
                     break
    #exostential binomial divistion
         elif funt == '/':
             for i in range(0,len(d)):
                 if d[i] / d[i] != 0:
                     if d[i] / d[s] != 0:
                         print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                         print(equation[1])
                         break
                 else:

                     print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                     print(equation[0])
                     break
    #exostential binomial multiplication
         elif funt == '*':
             for i in range(0,len(d)):
                 if d[i] * d[i] != 0:
                     if d[i] * d[s] != 0:
                         print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                         print(equation[1])
                         break
                 else:
                     print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                     print(equation[0])
                     break
 #Universal binomial
    elif quant == 'u':
     #Universal binomial addition
         if funt == '+':
             for i in range(0,len(d)):
                 if d[i] + d[i] == 0:
                     if d[i] + d[s] == 0:
                         print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                         print(equation[0])
                         break
                     else:
                         print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                         print(equation[1])
                         break
                 else:
                     print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                     print(equation[1])
                     break
     #Universal binomial subtraction
         elif funt == '-':
             for i in range(0,len(d)):
                 if d[i] - d[i] == 0:
                     if d[i] - d[s] == 0:
                         print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                         print(equation[0])
                         break
                     else:
                         print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                         print(equation[1])
                         break
                 else:
                     print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                     print(equation[1])
                     break
     #Universal binomial divistion
         elif funt == '/':
             for i in range(0,len(d)):
                 if d[i] / d[i] == 0:
                     if d[i] / d[s] == 0:
                         print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                         print(equation[0])
                         break
                     else:
                         print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                         print(equation[1])
                         break
                 else:
                     print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                     print(equation[1])
                     break
     #Universal binomial multiplication
         elif funt == '*':
             for i in range(0,len(d)):
                 if d[i] * d[i] ==0:
                     if d[i] * d[s] == 0:
                         print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                         print(equation[0])
                         break
                     else:
                         print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                         print(equation[1])
                         break
                 else:
                     print("(" + quant + ")" + v[0] + funt + v[1] + "= 0")
                     print(equation[1])
                     break
#output for Trinomials
elif varsL == 5:
    #print(d)
#Trinomial exostential
    if quant == 'e':
#Trinomial exostential addition
        if funt == '+':
            for i in range(0,len(d)):
                if d[0] + d[i] != d[s]:
                    if d[1] + d[i] != d[t]:
                        #Ex. assume 1 + 2 = 3
                        print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                        print(equation[1])
                        break
                    else:
                        print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                        print(equation[0])
                        break
                else:
                    print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                    print(equation[0])
                    break
#Trinomial exostential subtraction
        elif funt == '-':
            for i in range(0,len(d)):
                if d[0] - d[i] != d[s]:
                    if d[1] - d[i] != d[t]:
                        #Ex. assume 1 + 2 = 3
                        print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                        print(equation[1])
                        break
                    else:
                        print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                        print(equation[0])
                        break
                else:
                    print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                    print(equation[0])
                    break
#Trinomial exostential divistion
        elif funt == '/':
            for i in range(0,len(d)):
                if d[0] / d[i] != d[s]:
                    if d[1] / d[i] != d[t]:
                        #Ex. assume 1 + 2 = 3
                        print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                        print(equation[1])
                        break
                    else:
                        print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                        print(equation[0])
                        break
                else:
                    print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                    print(equation[0])
                    break
#Trinomial exostential multiplication
        elif funt == '*':
            for i in range(0,len(d)):
                if d[0] * d[i] != d[s]:
                    if d[1] * d[i] != d[t]:
                        #Ex. assume 1 + 2 = 3
                        print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                        print(equation[1])
                        break
                    else:
                        print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                        print(equation[0])
                        break
                else:
                    print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                    print(equation[0])
                    break
#Trinomial Universal
    elif quant == 'u':
#Trinomial Universal addition
        if funt == '+':
            for i in range(0,len(d)):
                if d[0] + d[i] == d[s]:
                    if d[1] + d[i] == d[t]:
                        #Ex. assume 1 + 2 = 3
                        print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                        print(equation[0])
                        break
                    else:
                        print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                        print(equation[1])
                        break
                else:
                    print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                    print(equation[1])
                    break
#Trinomial Universal subtraction
        elif funt == '-':
            for i in range(0,len(d)):
                if d[0] - d[i] == d[s]:
                    if d[1] - d[i] == d[t]:
                        #Ex. assume 1 + 2 = 3
                        print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                        print(equation[0])
                        break
                    else:
                        print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                        print(equation[1])
                        break
                else:
                    print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                    print(equation[1])
                    break
#Trinomial Universal divistion
        elif funt == '/':
            for i in range(0,len(d)):
                if d[0] / d[i] == d[s]:
                    if d[1] / d[i] == d[t]:
                        #Ex. assume 1 + 2 = 3
                        print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                        print(equation[0])
                        break
                    else:
                        print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                        print(equation[1])
                        break
                else:
                    print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                    print(equation[1])
                    break
#Trinomial Universal multiplication
        elif funt == '*':
            for i in range(0,len(d)):
                if d[0] * d[i] == d[s]:
                    if d[1] * d[i] == d[t]:
                        #Ex. assume 1 + 2 = 3
                        print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                        print(equation[0])
                        break
                    else:
                        print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                        print(equation[1])
                        break
                else:
                    print("(" + quant + ")" + v[0] + funt + v[1] + "=" + v[2])
                    print(equation[1])
                    break
        else:
            print("That was not a valid input")
      #run through all the domains inside of the equation array for the vars[]
#if statement to make sure the domain is only int values & increases
#if statement to determine if u or e was entered
#if all statements pass then continue...
#Quantify the given variables within the context of the...
#function, domain, and quantifiers.
#Output the truth value as T or F.
  #print()
#exit=input("Would you like to try again?(y/n): ")
#if exit=='n':
    #print("Bye")
    #break
