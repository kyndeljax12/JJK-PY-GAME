#For my game I'm doing based on favorite anime which is Jujustu Kaisen
#I'm try use compnents from the series as choice and also character
#Reusing old code from my first choose your own adventure game because I wanted add some mechanics 
# Mechanics I would like to add color to the names and fighting mechanics and maybe add more to the story as a whole 
#This is a personal project for me 

#Using Constants for Varibables so easy to write

import random
TEACHER="Satoru Gojo"
HEALTH = 100;

def intro():
    print("You walk around Tokyo station looking for white haired man with Blindfold")
    print("You just enrolled into school that will help learn how use your abilites because you've been seeing curses")
    print("Unknown-Hello I'm your teacher "+TEACHER)

def get_name(): 
    print()
    print(TEACHER +"- What your name:")
    name=input("Type your name:")
    return name

#Simple explanation of what a curse Technique is like super power
#But its uses this stuff called Curse energy
def curse_technique(name): 
    print(TEACHER+"- "+name+" Welcome Jujustu Tech where you will learn to be a Jujustu Sorcerer")
    print(TEACHER+" - Before we meet your classmates I need to know your curse technique, "+name)
    print(TEACHER+" - For example mine is the Limitless and the six eyes")
    print()
    print("Choose what Curse technique you would like")
    print("Option 1 Curse tool user")
    print("Option 2 10 shadows user")
    print("Option 3  Blood Malipulation")
    print("Option 4 Cuse Malipulation")
    print("Option 5 Curse Speech")
    print("Option 6 the Limitless")
    cursetechnique=input("Type the option number you would like:")

    if cursetechnique == "1":
        print(TEACHER+" - Huh really? Just like my other student Maki Zenin")
        print(TEACHER+" - Just dont't be mean like her")
        print(TEACHER+" - Well then you need to pick a wepon")
        print()
        print("Option 1 Black blade Katana")
        print("Option 2 a staff ")
        print("Option 3 Slaughter Demon which is a dagger")
        weapon=input("Type name of Weapon you would like:")
        if weapon == "Black blade Katana":
            print(TEACHER+" - Katana are always good option")
        elif weapon == "A Staff":
            print(TEACHER+" - Wow what boring option but okay")
        elif weapon == "Slaughter Demon":
            print(TEACHER+" - Nice don't tell Maki that I'm letting use this")
        else:
            print("Please give valid answer")
            return curse_technique()
        
        return "Curse tool User"+ " and my weapon is " +weapon

    elif cursetechnique == "2":
        print(TEACHER+" - Like your fellow classmate Megumi Fushigoro maybe you some Zenin blood in you")
        return "10 Shadows Technique"
    
    elif cursetechnique == "3":
        print(TEACHER+" - Well I guess I won't get paper cut around you then")
        return "Blood Maluplation"
    
    elif cursetechnique == "4":
        print(TEACHER+" - ...")
        print(TEACHER+" - Reminds me of someone I use to know")
        return "Curse Malputlation"
    
    elif cursetechnique == "5":
        print(TEACHER +" - Well then you don't talk much huh. If you do you could hurt people")
        print(TEACHER+ "Lucky for you we have Student name Toge Inumaki who can help you controll it")
        return "Curse Speech"
    
    elif cursetechnique =="6":
        print(TEACHER+" - We must be related")
        return "The Limitless"
    
    else:
        print("Please choose a valid option")
        return curse_technique(name)


# I wanted make a simple if statement 
def meeting_classmates(name, cursetechnique):
    print()
    print(TEACHER+ " - Now that we got that sorted out lets go meet you classmates")
    print(TEACHER+" - Here they are. Would like me to intoduce you or do want introduce youselves ")
    introduction=input("Type yes or y to introduce yourself or type no or n if want Gojo to introduce you: ")
    
    if introduction =="yes" or introduction=="y":
        print("Hello my name is "+name+" and my curse technique is "+cursetechnique )
    elif introduction=="no" or introduction=="n":
        print(TEACHER+" - Hey kids this is "+name+" and there curse techinique is "+ cursetechnique)
    else:
        print("Invalid answer")
        return meeting_classmates(name,cursetechnique)
   
    print("Yuji - Hello I'm Yuji Itadori it very nice to meet you "+name)
    print("Megumi - Hi I'm Megumi Fushigoro")
    print("Nobara - I don't care who you are but I'm Nobara Kugisaki")

def taking_on_curses(name,cursetechnique):
    print()
    print(TEACHER+" - So since " + name + " is new here I gonna put you in sitution that gonna test your abilties")
    print(TEACHER+" - Yuji, Megmumi, Nobara you can tag along if would like so you show newbie how it done")
    print("Yuji - I will go for support")
    print("Memgumi - I will stay behind it was nice to meet you "+name)  
    print("Nobara - Don't get killed newbie")
    print(TEACHER+" - Don't worry you won't get killed")

#I was looking at examples of code for choose your adventure games and this one game implemented choice that take to whole differnt function
#So I wanted to try it 
def choose_a_path(name,cursetechnique):
    print()
    print(TEACHER+" - So this building has a supposed level 3 curse in it so I need both find it a beat it or run come get me")
    print("Yuji - So what entrance would you like to take front or the back")
    entrance= input("Type back or front for which rout you like to take: ")

    if entrance== "back" or entrance=="Back":
        print()
        print("Yuji - Sounds like good idea the curse might guarding th front")
        go_back(name,cursetechnique)

    elif entrance=="front" or entrance=="Front":
        print()
        print("Yuji - Okay sounds good we might suprise it")
        go_front(name,cursetechnique)
    
    else:
        print("Invalid answer")
        choose_a_path()

#I wanted to make where there hit system to fight the curse but I couldn't figure it out
#So decide for go_back and go_front that they have different diffcaultie of curseto make choiced matter
def go_back(name,cursetechnique):
    print()
    print("Yuji - Okay were in looks like there hallway we need go through I bet down there")
    print("As you walk down the hall the curse suprises you and Yuji")
    print("Yuji - I thought we'd catch it by suprise but do want to take it on or get Gojo and I will stall")
    fight_or_flight=input("Type fight or run: ")

    if fight_or_flight=="fight" or fight_or_flight=="Fight":
        print()
        print("Yuji - Okay I punch it then you hit with your "+ cursetechnique)
        print("You hit with "+ cursetechnique+" defeat it easily")
        print("Yuji - Nice job Gojo will be happy")
    
    elif fight_or_flight=="run" or fight_or_flight=="Run":
        print()
        print("Yuju - Okay go get Gojo I will stall")
        print("You run out in a panick to get Gojo")
        print("You bring Gojo to the scene to Yuji already defeated the curse")
        print(TEACHER+" - It's okay just asscess the sitution better next time")
    
    else:
        print("Invalid Input")
        go_back()

def go_front(name,cursetechnique):
    print()
    print("Yuji - Okay going the front that a good idea")
    print("As you walk into the building and you find the curse is just sitting there")
    print("You see Yuji running at the curse to punch it but he thrown by the curse into wall knocked out")
    print("Now you set to choice whether you fight it or go get Gojo")
    fight_or_flight=input("Type fight or run: ")

    if fight_or_flight=="fight" or fight_or_flight=="Fight":
        print()
        print("The curse is not grade three curse it more like a grade 1 or special grade")
        print("The curse compleltly takes you out. You wake up in pain with Gojo standing over you")
        print(TEACHER+" - You got pretty beat up "+name+" next time just go get me ")
    
    elif fight_or_flight=="run" or fight_or_flight=="Run":
        print()
        print("As you run away you notice that curse is following you")
        print("Lucky for you Gojo right outside and Gojo ")
        print(TEACHER+" - Good thing you come and got me you could have been seriously injured")
        print(TEACHER+" - lets go get Yuji")
    
    else:
        print("Invalid Input")
        go_front()

 #The ending for the game    
def ending(name,cursetechnique):
    print()
    print(TEACHER+" - Well what first day huh, "+name)
    print(TEACHER +" - Once you learn how to master your "+ cursetechnique+" I see you being pretty strong")
    print(TEACHER+" - but not stong as me ")
    print("Thank you for playing my Jujustu Kaisen choose you own adventure game")


#This fuction run the whole game    
def main():
    intro()
    name=get_name()
    cursetechnique=curse_technique(name)
    meeting_classmates(name, cursetechnique)
    taking_on_curses(name,cursetechnique)
    choose_a_path(name,cursetechnique)
    ending(name,cursetechnique)
    

main()
    
