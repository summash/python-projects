# default function argument
def average(a, b):
    print("the avearage is= ", (a+b)/2)
average(4, 6)
def function_name(a=8, b=9):
    print("the sum is=", a+b)
function_name(b=6)  # we can also change the value
# keyword function argument
average(b=21, a=18)  # the order of the varaibles does not matter
# required arguments
def function(a, b, c, d=1):
    print("area of the quadrilateral=", (a*b*c*d), "meter_sq")
function(a=4, b=2, c=2)
# variable length argument
def average(*numbers):
    for i in numbers:
        sum = 0
        sum = sum+i
#rint("average is", sum/len(numbers))
average(1,2,3)
