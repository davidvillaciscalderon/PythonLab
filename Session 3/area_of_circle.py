#Author Emily Keiser

def exponent(x):
    return int(x)*int(x)

a=raw_input ("Enter radious: ")

def multiplication (x):
    return exponent (int(x))*(3.14)

print multiplication(a)
'''
import math
def areacircle(x):
    return 3.14*math.pow(int(x),2)
r=raw_input("Enter variable r: ")
print (areacircle (r))
def saveResult(result):
    f=open('result.txt','w')
    f.write(result)
    f.close()
saveResult(str(areacircle(r)))

'''