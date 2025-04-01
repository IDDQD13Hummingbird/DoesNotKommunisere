################################################################################
## Pant Mini-Game
################################################################################

# Define the background for the pant minigame
image bg pant_machine = "images/PantMiniGame/BG/bg_pant_machine.png"

# Define image paths with the correct filenames that are in the directory
image bottle_plastic_crushed:
    "images/PantMiniGame/bottles/bottle_plastic_crushed.png"

image bottle_cola_empty:
    "images/PantMiniGame/bottles/bottle_cola_empty.png"

image bottle_plastic_crushed2:
    "images/PantMiniGame/bottles/bottle_plastic_crushed2.png"

image bottle_water:
    "images/PantMiniGame/bottles/bottle_water.png"

image bottle_glass_cola:
    "images/PantMiniGame/bottles/bottle_glass_cola.png"

# Define a transform to resize the bottle images
transform bottle_size:
    size (200, 200)  # Set maximum size while maintaining aspect ratio
    zoom 0.5         # Scale down to 50%

init python:
    # Dictionary of bottles with their pantable status
    bottles = {
        "plastic_crushed": {"image": "bottle_plastic_crushed", "pantable": False, "value": 2},
        "cola_empty": {"image": "bottle_cola_empty", "pantable": True, "value": 3},
        "plastic_crushed2": {"image": "bottle_plastic_crushed2", "pantable": True, "value": 2},
        "water_bottle": {"image": "bottle_water", "pantable": False, "value": 2},
        "glass_cola": {"image": "bottle_glass_cola", "pantable": False, "value": 3}
    }
    
    def start_pant_game():
        global game_bottles, player_score, bottles_remaining
        # Shuffle and select bottles for this game session
        import random
        available_bottles = list(bottles.keys())
        random.shuffle(available_bottles)
        game_bottles = available_bottles[:5]  # Take 5 random bottles
        player_score = 0
        bottles_remaining = len(game_bottles)

    def process_bottle(bottle_id, is_pantable):
        global player_score, bottles_remaining
        correct_choice = bottles[bottle_id]["pantable"] == is_pantable
        
        # Debug information that will be displayed
        renpy.notify(f"Bottle: {bottle_id}, Pantable: {bottles[bottle_id]['pantable']}, Your choice: {is_pantable}, Correct: {correct_choice}")
        
        if correct_choice:
            if is_pantable:
                # Correct pantable bottle
                player_score += bottles[bottle_id]["value"]
                renpy.notify(f"Correct pantable! +{bottles[bottle_id]['value']} points!")
            else:
                # Correctly identified as not pantable
                player_score += 1  
                renpy.notify("Correct non-pantable! +1 point!")
        else:
            # Wrong choice
            renpy.notify("Wrong choice, no points.")
            pass
        
        bottles_remaining -= 1
        
        if bottles_remaining <= 0:
            # Game over, return to calling label
            renpy.jump("pant_game_result")

screen pant_game():
    # Add a full screen background that completely covers the 1280x720 resolution
    add "bg pant_machine":
        size (1920, 1080)
        xalign 0.5
        yalign 0.5
    
    # Main frame for the gameplay elements
    frame:
        background "#000000"  # Solid black background 
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 600
        
        vbox:
            spacing 20
            xfill True
            yfill True
            
            text "Pant Sorting Game" size 40 xalign 0.5 yalign 0.0
            
            # Create a dedicated area for the bottle image
            frame:
                background None
                xalign 0.5
                yalign 0.3
                xsize 300
                ysize 200
                
                $ current_bottle = game_bottles[len(game_bottles) - bottles_remaining]
                $ current_image = bottles[current_bottle]["image"]
                
                # Display current bottle with reduced size
                add current_image at bottle_size:
                    xalign 0.5  # Towards the right
                    yalign 0.5  # Towards the top
            
            # Game status below the bottle
            text "Score: [player_score]" size 30 xalign 0.5
            text "Bottles remaining: [bottles_remaining]" size 30 xalign 0.5
            
            # Add a spacer that will push the buttons to the bottom
            null height 70
            
            # Choice buttons at the bottom of the frame
            hbox:
                xalign 0.5
                yalign 1.0
                spacing 150
                
                textbutton "Pantable" action Function(process_bottle, current_bottle, True) xpadding 40 ypadding 20
                textbutton "Not Pantable" action Function(process_bottle, current_bottle, False) xpadding 40 ypadding 20

label pant_minigame:
    $ start_pant_game()
    
    # No need for scene command since we add background in the screen
    with fade
    
    "Welcome to the pant sorting game!"
    "Sort bottles correctly to earn money."
    "Pantable bottles are worth more, but make sure you sort them correctly!"
    
    call screen pant_game
    
label pant_game_result:
    scene
    with fade
    
    if player_score >= 10:
        "Great job! You earned [player_score] kroner from panting!"
        "You're a natural at recycling!"
    elif player_score >= 5:
        "Not bad! You earned [player_score] kroner from panting."
        "With a bit more practice, you'll be a panting expert!"
    else:
        "You earned [player_score] kroner from panting."
        "Keep practicing to learn which bottles are pantable!"
    
    "Thanks for playing the pant sorting game!"
    
    jump level_choose  # Return to level selection 