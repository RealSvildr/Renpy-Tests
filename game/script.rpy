# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define A = Character("Aang", color="CC6600")
define K = Character("Katara", color="0066CC")
define S = Character("Sokka")
define narrator = Character(what_italic=True)
define slowdissolve = Dissolve(1.0)
define fastdissolve = Dissolve(0.5)

# The game starts here.

label start:
    scene intro1 with slowdissolve
    pause 1.0
    scene intro2 with slowdissolve
    pause 0.5
    scene intro3 with slowdissolve
    pause 0.5
    
    narrator"CLICK TO BEGIN"

    scene astorm1 with fastdissolve
    pause 2.5
    scene astorm2
    pause 1.5
    scene astorm3

    narrator "Aang shuddered and watched, wide eyed, as the seas below him churned and rose and fell with the typhoon."
    narrator "Cold, fat droplets of rain hit him in the face hard enough to sting, flung with such force by the gale. "
    
    scene astorm4
    
    narrator "The furious power of nature tossed his massive Sky Bison into the briny blue like a limp little toy, and all around him was the freezing water."
    
    scene astorm6

    narrator "All he could hear was the occasional panicked bellow from Appa, and the screaming whirling, storm all around."

    scene astorm5

    narrator "He couldn’t move, couldn’t breathe, there was no air, he had no idea how to get to the surface! "

    narrator "Appa, what about him?! How would he save his best friend?"
    narrator "He wanted to go home."
    narrator "He wanted to see Monk Geyatso again, if he drowned here he would never grow up, never have sex, never get married, never be the Avatar he knew the world needed, even if he didn’t want to be…"

    scene white with slowdissolve

    narrator "He felt a surge of energy, a sudden realization of what to do, so sudden Aang himself couldn’t have said what it was"
    narrator "and then freezing....freezing cold, and darkness."

    scene awake1 with fade

    narrator "Next thing he knew, he was breathing again. It felt odd somehow, like he hadn’t done it in a while, even though he had been doing it mere moments ago"
    narrator " like his chest was still getting used to the act of rising and falling that he’d been doing forever…"
    
    scene awake2 with slowdissolve
    narrator "It was still cold, but there was wind, and light stung his eyes as he opened them. "

    scene awake3 with slowdissolve
    narrator "The first thing he noticed, were the beautiful blue eyes staring back into his."
    narrator "The face of a girl he’d never seen before. She was very beautiful though."

    scene kahappy with slowdissolve
    narrator "Brown skin, Water Tribe maybe? Her brown hair was done up, except for 2 loops on either side of her face."
    narrator "She had cute, kissable lips, a dainty little nose, and nice cheeks, with just a hint of blush to them from the biting of the chilly, gentle arctic wind that surrounded them."

    scene search with slowdissolve
    narrator "It was then he noticed his surroundings."
    narrator "Ice… snow… water… huh. Well, this was different. He must have floated south or something? Yea… no other explanation really made since. "

    scene ashot with fastdissolve
    narrator "Pushing the wondering from his mind, he said to this pretty water tribe girl the first thing that came to his mind."

    menu:
        "Will you go penguin-sledding with me?":
            call choice1 from _call_choice1
            
        "Damn, you look really pretty!":
            call choice2 from _call_choice2
        

    return
label choice1:

    scene kaconfused
    K"Sure... "

    scene apen with fastdissolve
    pause

    return
label choice2:
    scene karaised
    K "huh"
    pause
    return