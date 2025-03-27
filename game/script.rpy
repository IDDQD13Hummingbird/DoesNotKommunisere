# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define anon = Character("Unknown", color = "#b0d7e3")
define dream = ImageDissolve("imagedissolve dream.png", 1.0, 64)
define thought = ImageDissolve("imagedissolve thought.png", 1.0, 64)
define crack = ImageDissolve("imagedissolve crack.png", 1.0, 64)
define p_nvl = Character("", kind=nvl)
$ i = 0
 
#screen debug_button():
#    imagebutton:
#        xalign 0.7
#        ycenter 0.06 
#        auto "gui/debug_button.png" action OpenURL("https://www.patreon.com/bePatron?u=52492546")
# define debug_button = ImageButton "gui/debug_button.png" xalign 0.7 ycenter 0.06 
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

label lmain_menu :
$ i = 0
show bg level_choose   ##add main navigation screen background here. 
menu:
        "Level select":
            jump level_choose
        "Useful sources":
            jump sources
        "Exit":
            jump end_game

label sources:
    "Useful information sourses :"
    ##call screen debug_button #action OpenURL("https://www.patreon.com/bePatron?u=52492546") 
    ##debug_button ("Patreon") action OpenURL("https://www.patreon.com/bePatron?u=52492546")
    p_nvl "Move to the Hamar Region - {a=https://hamarregionen.no/move-to-the-hamar-region/}{color=#ff0000}hamarregionen.no{/color}{/a}"
    p_nvl "Immigration office - {a=http://udi.no/en/}{color=#ff0000}UDI.no{/color}{/a}"
    p_nvl "Change adress or contact information, pay taxes - {a=https://www.skatteetaten.no/person/}{color=#ff0000}Skattetatten.no{/color}{/a}"
    p_nvl "Help finding job, getting medical help and financial support - {a=https://www.nav.no/}{color=#ff0000}NAV.no{/color}{/a}"
    nvl clear
    ##hide debug_button
    jump lmain_menu

label level_choose:
show bg level_choose
with dissolve
"Choose your level :"

menu:
    "Pant game" if i == 0:
        jump scenario_1
    "More content":
        jump scenario_2
    "Back to main menu":
        jump lmain_menu


label scenario_1:

    scene bg pant
    with crack
    "Have you ever bought a drink at the store and noticed that it suddenly costs two or three kroners extra?"
    "Ever wondered, ''What is this weird bottle tax? Is it somehow connected to that little <PANT> label?''"
    "In fact, it is - almost every plastic or aluminum beverage container in Norway has an additional cost, which we call ''PANT'', attached to it."
    "Reasons for that? To enforce recycling and to protect ecology."
    "Don't worry, though - you can get your money back by depositing the bottle at the store after you're done drinking."
    "Unfortunately, you can't gulp the entire content of the bottle at the registry and only pay for the price of the beverage. (We wish, though.)"

    scene bg start
    with fade

    "You've been walking through the school corridors, sipping on your drink..."

    "As a responsible member of society, you decided to do the best thing you can with the bottle, "

    "and throw it away into the appropriate trash bin, labeled with 'Bottles and Cans'."

    "When suddenly..."

    scene bg when_suddenly

    anon "Oi da. Can I have it?"

    label choice_1:
    scene bg when_suddenly
    with thought
    "An unknown person approaches and asks you for your bottle. What do you do in this situation?"

    menu:

        "Throw it. It's trash.":
            jump choice1_a

        "Whatever, they can have it.":
            jump choice1_b

        "I'm calling the authorities!":
            jump choice1_c

    label choice1_a:

        $ menu_flag = True

        scene bg choice_1a

        anon "Oh come ooon, maaan..."

        "In Norway, you have a right to exercise your free will over your property."
        "There's nothing wrong with your course of actions per se, but consider the following :"
        "What if they're going to dumpster dive for the bottle? They'll get dirty and spread diseases."
        "With that thought in mind, let's consider the situation again :"
        jump choice_1

    label choice1_b:

        $ menu_flag = False
        scene bg choice_1b

        anon "Thanks, mate! :D"

        "And with that, you contributed to panting."

        jump choice1_done

    label choice1_c:

        $ menu_flag = True

        scene bg choice_1c

        anon "WOAH, DUDE, CHILL OUT!"

        "In Norway, the police number is 112."
        "When in universities, however, it is adviced to memorize your campus securitas number. You can usually find it at the reception."
        "It doesn't matter, however, because neither of the two will appreciate getting a call over someone asking for your trash."
        "A penalty or imprisonment up to 3 years can apply for the police misinformation. (source : Lovdata.no)"
        "With that thought in mind, let's consider the situation again :"
        jump choice_1
        

    label choice1_done:

        # ... the game continues here.
    #if menu_flag:
    #    jump choice_1
    #else:
        "What is 'panting', you're asking? Well..."
        scene bg panting
        with dissolve

        "In Norway, it is not uncommon to observe others pick up beverage containers from the bins or public spaces. We call this phenomena ''Collecting pant'', or ''Panting''."
        "Panting is a family-friendly activity which involves gathering plastic bottles and exchanging them for money at the stores, and it is practiced by all social groups."
        anon "So, a gamified trash collection?"
        "So, a gamified trash collection."
        "It is disproportionately popular in big families, amongst kids, and with low-income individuals, because it helps cut living expenses."
        "With enough dedication, pant could cover your grocery bill for a week, with aspiring ''pant-ers'' regularly clocking 120-1100 kr per visit to the pant machine."
        "You should try it sometime! It's fun! You'll get paid! And it's appreciated!"

        anon "Okay, sounds cool and all, but is it really appropriate to scrouge through the trash bins?"
        "Well, let's explore that question further."

        scene bg start
        with fade

        jump level_choose
  

label scenario_2:

    "Nothing here yet!"
    "But you can help us make more content by answering our survey {a=https://docs.google.com/forms/d/e/1FAIpQLSefQgoA1e2YYXFHBURse9ahTnFvx6gCZZFeaYTwrObs_Nsd6A/viewform}{color=#ff0000}here{/color}{/a}!"
    "...just play the rest of the game, and come back to click on {a=https://docs.google.com/forms/d/e/1FAIpQLSefQgoA1e2YYXFHBURse9ahTnFvx6gCZZFeaYTwrObs_Nsd6A/viewform}{color=#ff0000}this text{/color}{/a}."
    $ i = 1
    jump level_choose

label end_game:
  # This ends the game.
    return
