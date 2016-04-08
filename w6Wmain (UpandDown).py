def UpandDown():

    soojin1=raw_input("Please write number : ")

    opportunity=raw_input("Please determine opportunity number : ")

    opportunity=int(opportunity)

    for i in range(opportunity):

        soojin1=int(soojin1)

        soojin2=raw_input("Please write number : ")

        soojin2=int(soojin2)

        if soojin1>soojin2:

            print "Up"

        elif soojin1<soojin2:

            print "Down"

        elif soojin1==soojin2:

            print "Good!"

            break

        print "Game over"

 

UpandDown()

"""
@startuml
 
 
 
  
 
 
 title Up and Down Game
 
 
 
  
 
 
 
start
 
 
 
:soojin1 :Please write your number(=soojin1);
 
 
 
:soojin2 :Please determine opportunity number(=x) and Please write your number(=soojin2);
 
 
 
  
 
 
 
while( )
 
 
 
if (non soojin1=soojin2) then (soojin1<soojin2)
 
 
 
:Up;
 

else (soojin1>soojin2)
 
 
 
:Down;
 
 
 
endif
 
 
 
endwhile
 
 
 
:chance is over or soojin1=soojin2;
 
 
 
if ( ) then (over chance)
 
 
 
:End Game;
 
 
 
else (soojin1=soojin2)
 
 
 
:Good!;
 
 
 
endif
 
 
 
  
 
 
 
:Game Over;
 
 
 
  
 
 
 
@enduml
"""
 
 def lab6():
     UpandDown()
     
 def main():
     lap6()
if __name__=="__main__":
    main()
 
