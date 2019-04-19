#!/usr/bin/python

##LOOPS in Python

##For Loop
#---------------

for x in range(0,6):
    print x                #prints "0,1,2,3,4,5"each digit on diff line
                           # Again 4  space at start are imp
#--------------


## while loop
#--------------

i=0
while i<5:
    print i;            ## Loop runs five times and print values
    i=i+1;

#-------------




##if else  Loop

a=int(raw_input("Enter a number"))
b=int(raw_input("Enter a number"))

if a>b:
    print("a=%d is"%a,"greater than b=%d"%b)
else:
    print("b=%d"%b,"is greater than a=%d"%a)

##-------------


##if else if loop     ## just a demo prog equal to condition not considered

#---------------

a=int(raw_input("Enter a number"))

if a>100:
    print("a=%d is greater than 100"%a)
elif a>50:
    print("a=%d is 100>a>50"%a)
else:
    print("a=%d is Less than 50"%a)

#---------------



