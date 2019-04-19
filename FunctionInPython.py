#!/usr/bin/python

#function defination 

##Function Type 1 passing argument and return
#----------------
def fun1(a,b):  
    a=a+b       ## four spaces are IMP they counted as a "body"
    return a
#----------------

##Function Type 2 no argument no return
#----------------
def fun2():
    print"IN fun2"
#----------------

## Function type 3 Lamda function
#---------------
x=lambda a: a+10   #used for small expression Prog
#---------------


a=fun1(1,2)         ## function call and return
print"Value a=",a   ## print the result stored in 'a'
fun2()              ## fun2 call prints "IN fun2"
print x(10)         ## Lambda function call 
