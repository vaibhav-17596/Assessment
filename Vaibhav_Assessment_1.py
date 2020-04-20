# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:50:36 2020

@author: VAIBHAV SHARMA
"""
import math
def assign():
    num=int(input("Enter a number: "))
    fact=[]
    flag=False
    print(str(num)+" is a "+str(len(str(num)))+" digit number")
    if (num % 2) == 0:
        print(str(num)+" is an even number")
    else:
        print(str(num)+" is an odd number")
    
    for i in range(1, num + 1):
       if num % i == 0:
           fact.append(i)
    
    for i in range (0, len(fact)):
        if(fact[i]>=2 and fact[i] <num):
            flag=True
        print (fact[i], end =" ")
    print("are factors of "+str(num))
    
	#0 an 1 neithe rprime nr cmpsite
	#if length f factrs array >2 - cmpsite
    if(flag):
        print(str(num)+" is not a prime number")
    else:
        print(str(num)+" is a prime number")
        
    sr = math.sqrt(num)
    if((sr - math.floor(sr)) == 0):
        print(str(num)+" is a perfect square")
    else:
        print(str(num)+" is not a perfect square")
        
    print("Square of "+str(num)+" is "+str(num**2))
    print("Cube of "+str(num)+" is "+str(num**3))
    
assign()

#pow(num,2)
#round(sr,4) - if 4 not there, it will rund t the nearest integer


input as num
n = num
cunt = 0
while n>0:
	cunt = cunt + 1
	n = n//10

#Number f digits - cunt
#34//10 - 3 - trims the last digit

rt = math.sqrt(num)
if int(rt + 0.5) ** 2 == num:
	num is a perfect square
else:
	num is nt a perfect square