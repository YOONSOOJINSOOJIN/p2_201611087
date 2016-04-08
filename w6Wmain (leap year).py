def leapyear():

    year=raw_input("Please write year : ")

    year=int(year)

    if (year%4 == 0) and (year%100 != 0 or year%400== 0):

        print "leap year"

    else :

        print "not leap year"

 

leapyear()
"""
@startuml
 

 

 

 
title Leap Year
 

 
 
 

 
start
 

 
:user input year;
 

 
 
 

 
if(year%4==0)and (year%100 !=0 or year%400==0) then (yes)
 

 
 
 

:print Leap Year;
 

 

 

 
else (no)
 

 

 

 
:print Not Leap Year;
 

 


 
endif
"""

def lab6():
    leapyear()
    
def main():
    lab6()
if__name__=="__main__":
    main()
    
 
