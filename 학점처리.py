﻿marksTmp = raw_input('성적을 입력하세요 (0~100):')
marks = float(marksTmp)
print "입력 값은: ",marks

marks = raw_input("input 0~100 :") 
 def Convermarksgrade(marks): 
        if 90<=float(marks)<=100: 
            grade="A" 
        elif 80<=float(marks)<90: 
            grade="B" 
        elif 70<=float(marks)<80: 
            grade="C" 
        elif 60<=float(marks)<70: 
            grade="D" 
        else: 
            grade="F or input error" 
        return grade 
    result=Convermarksgrade(marks) 
    print "tour grade is %s " %result 
