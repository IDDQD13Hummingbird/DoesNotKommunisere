# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define anon = Character("Unknown", color = "#b0d7e3")
define dream = ImageDissolve("imagedissolve dream.png", 1.0, 64)
define thought = ImageDissolve("imagedissolve thought.png", 1.0, 64)
define crack = ImageDissolve("imagedissolve crack.png", 1.0, 64)
define p_nvl = Character("", kind=nvl)
define us_nvl = Character("Group 5", color = "#b0d7e3", kind=nvl)
transform slightleft:
    xalign 0.25
    yalign 1.0
 
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
us_nvl "Welcome to our \n''Survival guide for new students at INN''*!"
p_nvl "{i}*(name in development){/i}"
p_nvl "Press ''Level select'' to access content,"
p_nvl "''Useful sources'' for links to organisations \nthat can help you in Hamar,"
p_nvl "and ''Exit'' to go back to the Main menu."
us_nvl "Enjoy! :D"
menu:   
        "Level select":
            jump level_choose
        "Useful sources":
            jump sources
        "Exit":
            jump end_game

label sources:
    "Useful information sourses :"

    show screen patreon_button
    
    nvl clear

    p_nvl "Move to the Hamar Region - {a=https://hamarregionen.no/move-to-the-hamar-region/}{color=#ff0000}hamarregionen.no{/color}{/a}"
    p_nvl "Immigration office - {a=http://udi.no/en/}{color=#ff0000}UDI.no{/color}{/a}"
    p_nvl "Change adress or contact information, \npay taxes - {a=https://www.skatteetaten.no/person/}{color=#ff0000}Skattetatten.no{/color}{/a}"
    p_nvl "Help finding job, getting medical help \nand financial support - {a=https://www.nav.no/}{color=#ff0000}NAV.no{/color}{/a}"
    p_nvl "Apply for student credit - {a=https://lanekassen.no/nb-NO/}{color=#ff0000}lanekassen.no{/color}{/a}"
    nvl clear
    hide screen patreon_button
    jump lmain_menu

label level_choose:
show bg level_choose
with dissolve
"Choose your level :"

menu:
    "Pant game": 
        jump scenario_1
    "Pant sorting minigame":
        jump pant_minigame
    "More content"if i == 0:
        jump scenario_2
    "Back to main menu":
        jump lmain_menu


label scenario_1:
    $ loves_police = False
    scene bg pant
    with crack
    "Have you ever bought a drink at the store and noticed that it suddenly costs two or three kroners extra?"
    "Ever wondered, ''What is this weird bottle tax? Is it somehow connected to that little <PANT> label?''"
    "In fact, it is - almost every plastic or aluminum beverage container in Norway has an additional cost, which we call ''PANT'', attached to it."
    "Reasons for that? \nTo enforce recycling and to protect ecology."
    "Don't worry, though - you can get your money back by depositing the bottle at the store after you're done drinking."
    "Unfortunately, you can't gulp the entire content of the bottle at the registry and only pay for the price of the beverage. (We wish, though.)"

    scene bg start
    with fade

    "You've been walking through the uni's corridors, sipping on your drink..."

    "As a responsible member of society, you decided to do the best thing you can with the bottle and throw it away into the appropriate trash bin, labeled with 'Bottles/Flask'."

    "When suddenly..."

    scene bg when_suddenly

    anon "Oi da. Can I have it?"

    label choice_1:
    scene bg when_suddenly
    with thought
    "An unfamiliar student approaches and asks you for your bottle. What do you do in this situation?"

    menu:

        "Throw it. It's trash.":
            jump choice1_a

        "Whatever, they can have it.":
            jump choice1_b

        "I'm calling the authorities!":
            jump choice1_c

    label choice1_a:

        $ loves_police = False

        scene bg choice_1a

        anon "Oh come ooon, maaan..."

        "In Norway, you have a right to exercise your free will over your property."
        "There's nothing wrong with your course of actions per se, but consider the following :{w}What if they're going to dumpster dive for the bottle? They'll get dirty and spread diseases."
        "{i}With that thought in mind, let's consider the situation again :{/i}"
        jump choice_1

    label choice1_b:

        scene bg choice_1b

        anon "Thanks, mate! :D"

        "And with that, you contributed to panting."

        jump choice1_done

    label choice1_c:

        $ loves_police = True

        scene bg choice_1c

        anon "WOAH, DUDE, CHILL OUT!"

        "In Norway, the police number is 112. \nThe non-emergency police number is 02800."
        "When at INN, however, it is adviced to use your campus securitas number - 93495020. You will find it at the reception."
        "A penalty or imprisonment up to 3 years can apply for the police misinformation and misuse of 122 line (source : Lovdata.no), so make sure to call 02800 if it's not urgent."
        "All of this doesn't matter in our case, however, because neither of them all will appreciate getting a call over someone asking for your trash."
        "{i}With that thought in mind, let's consider the situation again :{/i}"
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
        "Panting is a family-friendly activity which involves gathering plastic bottles and exchanging them for money at the stores. \nIt is practiced by all social groups."
        anon "So, a gamified trash collection?"
        "So, a gamified trash collection."
        "It is disproportionately popular in big families, amongst kids, and with low-income individuals, because it helps cut living expenses."
        "With enough dedication, pant could cover your grocery bill for a week, with aspiring ''pant-ers'' regularly clocking 120-1100 kr per visit to the pant machine."
        "You should try it sometime! It's fun! \nYou'll get paid! And it's appreciated!"

        anon "Okay, sounds cool and all, but is it really appropriate to scrouge through the trash bins?"
        "Well, let's explore that question further."

        scene bg and_then
        with fade

        "You're walking through the hallways, and you see a youngster digging through the trash bins."
        "They're elbow deep in,{w} fishing out the bottles,{w} \nreally getting into the whole thing."
        label choice_2:
            scene bg and_then
            with thought
        "You feel indifferent to this. What shall you do?"

menu:
    "Where are their parents looking? \nCall the child services!":
        jump choice2_a

    "Okay, this is unacceptable. Scold 'em.":
        jump choice2_b

    "Yeah, you go, child! Earn that pocket money!":
        jump choice2_c


        label choice2_a:
            scene bg choice_2a
            anon "woah! chill, dude!"
            "Alerting barnevern leads to an investigation of child's parents over the potential abuse and mistreatment."
            "As a part of investigation, the child will be separated from the parents and interviewed in private. Some children will not be returned to their parents afterwards."
            "Here's the barnevern number - 116 111. \nOnly use it if you suspect the child to be in danger."
            "(P.s. : In Norway, child digging through the trash \n{b}does not{/b} equal to child being abused.)"
            "{i}With that thought in mind, let's consider the situation again :{/i}"
            $ if loves_police == False: loves_police = False 
            jump choice_2

        label choice2_b:
            scene bg choice_2b
            anon "woah!! don't talk to me like that!!"
            "Okay, this is something worth calling \nthe child protection over. {i}On you.{/i}"
            "In Norway, children protection laws prohibit verbal or physical abuse directed towards the children."
            "In case of doubt, refer to {a=https://www.bufdir.no/en/child-welfare-services/role/}{color=#ff0000}Bufdir{/color}{/a}."
            "{i}With that thought in mind, let's consider the situation again :{/i}"
            jump choice_2
            $ loves_police = False

        label choice2_c:
            scene bg choice_2c
            "Chill. Kid's doing his stuff. \nWho are we to touch someone else's child?"
            jump choice2_done
        #scene bg start
        #with fade
        label choice2_done:
            anon "I see, I guess people are really chill about it here."
            "True! But it's worth mentioning that even well-intended things \ncan be overdone."
            "Let's look through one last example:"
            scene bg friend
            with fade
            "You hang out at your friend's appartment, when suddenly..."
            scene bg hello
            "You notice piled up bottles on the windowstill."
            "In fact, you look around, and only notice more:"
            show rubbish at slightleft
            with vpunch
            "Bags of pant are laying around the room, unappelingly."
            hide rubbish
        label choice_3:
            scene bg hello
            with thought
        "You feel worried about your friend. What shall you do?"

menu:
    "Confront your friend about it harshly":
        jump choice3_a
    "Implore about your friend's mental well-being.":
        jump choice3_b
    "Offer to go pant them together!":
        jump choice3_c
    "There is no ''Calling the police''." if loves_police == True:
        jump choice_3

label choice3_a:
    scene bg wtf
    "''Wow, you {i}really{/i} live like this? \nI swear, bro, even pigs are more tidy.\nYo mama taught you nothing?''"
    "Your friend hides their face in an embarassment, gets up and leaves."
    "Generally, bullying a person with the issues of maintaining their living enviroment clean isn't a good approach."
    "Hoarding is a real problem, and is very mentally taxing on those dealing with it. Criticizing someone who might already hate themselves for it will not motivate them to change."
    "{i}With that thought in mind, let's consider the situation again :{/i}"
    jump choice_3
label choice3_b:
    scene bg wtf
    "''Bro are you okay? You need to talk?''"
    scene bg are_you_okay
    with dissolve
    "And so, you did talk. you found out about all the hardship your friend is dealing with, and generally was a really good listener."
    "After talking for hours, you got tired, and decided to sit down...{w} except, there's no place to drop and rest at because of all of the bottles."
    "A thought crossed your mind: maybe, all the bottles laying around are contributing to their bad mental state, \nand they need to deal with them first?"
    "{i}With that thought in mind, let's consider the situation again :{/i}"
    jump choice_3
label choice3_c:
    scene bg wtf
    "''Bro, let's go pant this! \nWe can get some ice cream together while we're at it!''"
    scene bg go_pant
    "You help your friend gather all of the bottles and put them into a grocery bag - typical for Norwegian panting."
    "{i}We'll add a proper tutorial on how to pant later.{/i}"
    jump choice3_done

label choice3_done:
    "Congratulations! Now you know how to adress the Pant.\nHope this will make your stay in Norway marginaly better."
    $ i = 0
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
