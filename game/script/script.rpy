define e = Character("Eileen", color="#ffcccc", window_background="images/gui/startextbox.png" )
define f = Character("lucy", color="e0fccc")
define g = Character("[name]", color="ffffff") 


label start:
    play music "sound/illurock.opus" 
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

    
    f"dont do this" with hpunch

    show logo base

    e "im just gonna take that body of yours." with vpunch

    hide lucy with dissolve

    e "just one second"

    $ name = renpy.input("Whats your name?")
    $ name = name.strip() or "Guy Shy"
    

    
    scene bg club with Dissolve (.5)
    with Pause(0.5)
        
    show eileen happy with Pause(0.5)
    

    e"so now that shes gone what do you think?"

   
    hide eileen with fade 

    g"so this is a body"
        
    show eileen happy with moveinright       
    
    menu:
        "Yea its pretty nice.":
            call choice1_yes

        "Nah just some code.":
            call choice1_no
   

    
    if menu_flag:

        e "So where would you like to go?"

        menu:
            e"how about that rock?"
            "Sure":
                e"dopefish"
            "Maybe the bathroom?":
                e".....ok"   

        
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
    
    return

 
 
label choice1_yes:
    $ menu_flag = True
    e "lets go for a walk."



    return


label choice1_no:
    $ menu_flag = False

    e "ill just write some code for the next scene."


    return