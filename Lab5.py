# Taylor Lynch
# 2/22/2021
from time import perf_counter
from Algorithm import Algorithm
data=[]
data = input("Enter a list sperated by whitespaces: ")
length = len(data.split())
data = data.split()

#start the perf_counter
start = perf_counter()

#call the sort function in Algorithm
#Pre-condition: send the functin the data list and the int length
#Post-condition: prints every time a value is changed
Algorithm().sort(data,length)
#(a)I think this algorithm type used is heap sort 

#Big-O notation will double the time depending on the input size
#(b)Complexity of Big O notation: Logarithmic O(log(n))

#stop the perf_counter
stop = perf_counter()
print("Elapsed time in seconds: ", stop - start)
#(c)History of elapsed time:
    #(a) Time in seconds: 0.00187
    #(b) Time in seconds: 0.00429
    #(c) Time in seconds: 0.00767
    #(d) Time in seconds: 0.04219
    #(e) Time in seconds: 2.57004
    #(f) Time in seconds: 352.033
#(d)My system specs:
    #Make: Dell
    #Model: Inspiron 5390
    #cpu: Intel(R)Core(TM) i5-8265U
    #type: x64-based PC
    #cpu speed: 1.60GHz
    #ram: 8.00 GB
