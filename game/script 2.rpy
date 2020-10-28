# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#ffcccc", window_background="gui/startextbox.png" )
define f = Character("lucy", color="e0fccc")
define g = Character("[name]", color="ffffff") 
# The game starts here.

label start:
    play music "illurock.opus" 
    "Wow, It`s really dark in here."
    "lucy" "Better watch out."
    e "Bruh whats good"
   
    scene bg cave with fade

    show eileen happy at right
    e"nah this aint that good"
    
    show lucy happy:
        xalign 0.0
        yalign 1.0
    show eileen happy with fade

    ##### These lines are part of the start label
    ##### they need to be indented correcly, for the code to understand it's still the start label
    f"dont do this" with hpunch

    show logo base

    e "im just gonna take that body of yours." with vpunch

    hide lucy with dissolve

    e "just one second"

    ### To create variables you don't need to start a python execution
    ### you can just use $
    #python: 
    #    name = renpy.input("Whats your name?")
    #    name = name.strip() or "Guy Shy"

    $ name = renpy.input("Whats your name?")
    $ name = name.strip() or "Guy Shy"
    

    
    scene bg club with Dissolve (.5)
    with Pause(0.5)
        
    show eileen happy 

    e"so now that shes gone what do you think?"

    ## when you create a pause out of nowhere you can just use:
    pause .5
    #with Pause(0.5)


    hide eileen with fade 

    g"so this is a body"
        
    show eileen happy with moveinright       
    
    menu:
        "Yea its pretty nice.":
            call choice1_yes

        "Nah just some code.":
            call choice1_no
    ##### Part 1 

    ### As  we are not using the choice1_done anymore, you can continue the code after the menu here.

    ###### Here indent again as it was all part of the label choice1_done
    ###### And now is part of the start
    if menu_flag:

        e "So where would you like to go?"

        menu:
            e"how about that rock?"
            "Sure":
                e"dopefish"
            "Maybe the bathroom?":
                e".....ok"   

        # You can continue the code here no need to set another if at the bottom, as it tests the same parameter.
        
        ### This does nothing
        ###$ True
        scene bg lecturehall
        e"im sure the bathroom is here somewhere"
        e"ill go look for it"
        hide eileen with dissolve

        show lucy happy:
            xalign 1.0 yalign 0.0
            pause 1.0
            xalign 0.0
            pause 1.0
            repeat

        f"run.....you fools"


    else:
        e "Im just gonna teleport you!."

        menu:
            e"come one get your binary ass over there"
            "NOOOOOOOO":
                e"you aint got a choice cholo"
            "you could ask nicely":
                e"Please get your binary ass over there?"
    
        ### This does nothing
        ### $ False
        scene bg uni
        show eileen happy
        e"where do you think youre going bruv?"
        hide eileen with dissolve

        show lucy happy:
            xalign 0.25
            yalign 1.0

        f"run my dude "

        hide lucy with hpunch

    show eileen happy:
        xalign .3 yalign .7
        linear 1.0 xalign .7 yalign .3
        linear 1.0 xalign .3 yalign .7
        repeat
        
    e "haahahaha youll never get away"
    
    # This ends the game.
    return

    ####### NOTE
    ### Renpy uses indent spaces to identify where what does
    #e.g:
    #menu: ## This Start a Menu
    #   "Choice 1": #The first choice as You can see it has 4 extra spaces at the beggining, that means this choice is inside menu
    #       $ var1 = 1 ## This has 4 extra spaces that means this line is inside the "Choice 1", and 8 spaces if you compare to menu.
    ## It's better to give an extra line of space after ending a menu or something else to make it easier to understand that it's not part of the menu.
    #pause # as this one doesn't have extra spaces it'll execute after the menu ended doesn't matter how many choices or  lines the menu has. 
 
label choice1_yes:
    $ menu_flag = True
    e "lets go for a walk."

    ## This is calling a different label instead of returning to the start label
    ## to return instead use 'return' at the end and instead of using 'jump' use call
    #jump choice1_done

    return


label choice1_no:
    $ menu_flag = False

    e "ill just write some code for the next scene."

    ## This is calling a different label instead of returning to the start label
    ## to return instead use 'return' at the end and instead of using 'jump' use call
    #jump choice1_done
    return