#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
         print(f"{counter}")
         counter -= 1
    print("Happy New Year!")
   
def square_integers(int_list):
    squared_int = [pow(integer,2) for integer in int_list]
    return squared_int

def fizzbuzz():
    for i in range(100):
        i = i+1
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(f"{i}")
    


