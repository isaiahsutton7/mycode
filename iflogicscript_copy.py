#!/usr/bin/env python3

input("What anime character are you? Press enter to find out! ")

msg = 'Your anime character is '

anime = float(input('How old are you? ')) #First question

if anime >= 27: 
    kids= float(input('How many kids do you have? ')) #If older than 27 ask how many kids
    if kids >= 3:
        newmsg = "I like that name! You get my personal favorite: Shisui Uchiha."
        question= input("What's your oldest child's first name? ")
        if question.lower() == 'isaiah': 
            msg = newmsg
        else:
            msg = msg + 'Kakashi Hatake'
    elif kids >= 1:
        msg = msg + 'Lady Tsunade'
    elif kids == 0:
        sorry= input("Are you married? ") #If no kids ask if married
        if sorry.lower() == "yes":
            card= float(input("What is your credit card number?(No spaces) ")) #If married ask for credit card
            if card >= 1:
                back= float(input("What is the 3 digit code on the back? ")) 
                if back >= 99:
                    msg= "Thanks for buying my new PC"
                else:
                    msg = msg + 'Deku'
            else:
                msg = msg + 'Goku' #If no card number is provided
        elif sorry.lower() == "no":
            msg = msg + 'Madara Uchiha'
        else: #If the answer isnt yes or no you will get the following msg
            msg = "If you got here you're special. Your anime character is Naruto."
    else:
        msg = msg + 'Jiraiya'

elif anime >= 21:
    hot= float(input('Rate Jhene Aiko 1-10: ')) #Jhene Aiko is a 10 forever and always
    if hot >= 10:
        phone = input("Apple or Android? ")
        if phone.lower() == "apple":
            msg = "You have extremely good taste. You're my personal favorite: Shisui Uchiha"
        elif phone.lower() == "android":
            msg = msg + 'Hashirama Senju'
        else:
            msg = msg + "Naruto... but only when he's being annoying"
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
