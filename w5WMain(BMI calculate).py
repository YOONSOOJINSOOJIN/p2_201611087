﻿height=input ("input user height 1.8(m):")

weight=input ("input user weight 70(kg):")

BMI=weight/(height*height)

if BMI<=18.5:

    print "Underweight"

elif 18.5<BMI<=23:

    print "Normalweight"

elif 23<BMI<=25:

    print "Overweight"

elif 25<BMI<=30:

    print "Obesity"

elif BMI>30:

    print "An extremly obese"
