

userA=raw_input('userA input scissor, rock, paper : ')

userB=raw_input('userB input scissor, rock, paper : ')

if userA=='scissor':

    if userB=='rock':

        print "%s" %"UserB Win"

    elif userB=='paper':

        print "%s" %"UserA Win"

    else:

        print "%s" %"Draw"

elif userA=='rock':

    if userB=='scissor':

        print "%s" %"UserA Win"

    elif userB=='paper':

        print "%s" %"UserB Win"

    else:

        print "%s" %"Draw"

elif userA=='paper':

    if userB=='scissor':

        print "%s" %"UserB Win"

    elif userB=='rock':

        print "%s" %"UserA Win"

    else:

        print "%s" %"Draw"
