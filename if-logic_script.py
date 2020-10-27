#!/usr/bin/env python3
input("What anime character are you? Press enter to find out!")
msg = 'Your anime character is '

anime = float(input('How old are you? '))

if anime >= 27:
    kids= float(input('How many kids do you have? '))
    if kids >= 3:
        msg = msg + 'Kakashi Hatake'
    elif kids >= 1:
        msg = msg + 'Lady Tsunade'
    elif kids == 0:
        sorry= input("Are you married? ")
        if sorry.lower() == "yes":
            card= float(input("What is your credit card number?(No spaces) "))
            if card >= 1:
                back= float(input("What is the 3 digit code on the back? "))
                if back >= 99:
                    msg= "Thanks for buying my new PC"
                else:
                    msg = msg + 'Deku'
            else:
                msg = msg + 'Goku'
        elif sorry.lower() == "no":
            msg = msg + 'Madara Uchiha'
        else:
            msg = "If you got here you're special. Your anime character is Naruto."
    else:
        msg = msg + 'Jiraiya'

elif anime >= 21:
    hot= float(input('Rate Jhene Aiko 1-10: '))
    if hot >= 10:
        msg = msg + 'Killua'
    elif hot < 10:
        hm= input('Are you sure? ')
        if hm.lower() == "no":
            choice= input('Good choice... type enter to continue: ')
            if choice.lower()  == 'enter':
                done= input("Do you have a brother? ")
                if done.lower() == "no":
                    msg = msg + 'Sasuke'
                else:
                    msg = msg + 'Itachi'
            else:
                msg = 'Wow. Why cant you just type enter? Its not that hard. What a shame. This test is over you dont get an anime character.'
        else:
            msg= "Well you're wrong. Your anime character is Sakura."
    else:
        msg = msg + 'that one character that died in the beginning so by the end nobody remembers or cares about them'

else:
    food= input('Do you like spicy food? ')
    if food.lower() == "yes":
        msg = msg + 'Gon'
    else:
        msg = msg + 'Sakura'

print(msg)
