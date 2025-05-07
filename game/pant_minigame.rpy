################################################################################
## Pant Mini-Game
################################################################################

# Define the background for the pant minigame
image bg pant_machine = "images/PantMiniGame/BG/bg_pant_machine.png"
image bg pant_intermission = "images/PantMiniGame/BG/PantIntermission.jpg"
image bg pant_intermission_accepted = "images/PantMiniGame/BG/pantintermissionaccepted.png"
image bg pant_intermission_not_accepted = "images/PantMiniGame/BG/pantintermissionnotaccepted.png"

# Define image paths with the correct filenames that are in the directory
image bottle_plastic_crushed = "images/PantMiniGame/bottles/bottle_plastic_crushed.png"
image bottle_cola_empty = "images/PantMiniGame/bottles/bottle_cola_empty.png"
image bottle_plastic_crushed2 = "images/PantMiniGame/bottles/bottle_plastic_crushed2.png"
image bottle_water = "images/PantMiniGame/bottles/bottle_water.png"
image bottle_glass_cola = "images/PantMiniGame/bottles/bottle_glass_cola.png"

# Define UI elements for drag-and-drop
image pant_zone = Frame("gui/button/idle_background.png", 10, 10)
image discard_zone = Frame("gui/button/idle_background.png", 10, 10)

# Define a transform to resize the bottle images
transform bottle_size:
    size (300, 300)  # Increased size while maintaining aspect ratio
    zoom 0.9         # Increased zoom from 0.8 to 0.9
    alpha 0.9        # Slight transparency

# Define transforms for pant and discard zones
transform pant_zone_pos:
    xalign 0.2
    yalign 0.7
    
transform discard_zone_pos:
    xalign 0.8
    yalign 0.7

# Define a transform for background images to ensure they cover the screen
transform bg_fullscreen:
    size (1920, 1080)
    xalign 0.5
    yalign 0.5

init python:
    # Dictionary of bottles with their pantable status
    bottles = {
        "plastic_crushed": {"image": "bottle_plastic_crushed", "pantable": False, "value": 2},
        "cola_empty": {"image": "bottle_cola_empty", "pantable": True, "value": 3},
        "plastic_crushed2": {"image": "bottle_plastic_crushed2", "pantable": False, "value": 2},
        "water_bottle": {"image": "bottle_water", "pantable": False, "value": 2},
        "glass_cola": {"image": "bottle_glass_cola", "pantable": False, "value": 3}
    }
    
    def start_pant_game():
        global game_bottles, player_score, bottles_remaining, game_finished, show_results
        # Shuffle and select bottles for this game session
        import random
        available_bottles = list(bottles.keys())
        random.shuffle(available_bottles)
        game_bottles = available_bottles[:5]  # Take 5 random bottles
        player_score = 0
        bottles_remaining = len(game_bottles)
        game_finished = False
        show_results = False  # New variable to control when to show results

    def process_bottle(bottle_id, is_pantable):
        global player_score, bottles_remaining, game_finished
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
        
        # Set game_finished flag when all bottles are processed
        if bottles_remaining <= 0:
            game_finished = True
        # Otherwise, continue with next bottle

    def show_game_results():
        global show_results
        show_results = True
        # If we want to use NVL style instead:
        # renpy.show_screen("pant_results")

# This is called when the draggable is dropped
init python:
    def draggable_dropped(drags, drop):
        # drags is a list of all draggables (just one in our case)
        # drop is where it was dropped, or None if dropped somewhere else
        
        if not drop:
            # Not dropped on a target, return to starting position
            return
        
        current_bottle = game_bottles[len(game_bottles) - bottles_remaining]
        
        if drop.drag_name == "pant_zone":
            # Dropped on the pant zone
            process_bottle(current_bottle, True)
        elif drop.drag_name == "discard_zone":
            # Dropped on the discard zone
            process_bottle(current_bottle, False)
        
        # If we still have bottles left, reset drag position for next bottle
        if bottles_remaining > 0:
            # Reset position to center for the next bottle
            drags[0].snap(825, 360)  # RESET POSITION - Matches centered bottle position
            # Tell the drag system we've handled this
            return True
        else:
            # If we're out of bottles, show the "See Results" button but don't jump yet
            # The game_finished flag is already set in process_bottle
            return True

label pant_minigame:
    $ start_pant_game()
    
    # Show the accepted image first
    scene bg pant_intermission_accepted at bg_fullscreen
    with fade
    
    "Welcome to the pant sorting minigame!"
    "In Norway, certain bottles and cans can be returned for a refund, known as 'pant'."
    
    # Switch to the not accepted image when explaining limitations
    scene bg pant_intermission_not_accepted at bg_fullscreen
    with dissolve
    
    "Not all containers are eligible - only those marked with the official pant symbol."
    "In this game, you'll need to sort which bottles are pantable and which aren't."
    "Drag each bottle to the correct zone: PANT for pantable bottles, DISCARD for non-pantable ones."
    "You'll earn points for correct sorting - pantable bottles are worth more!"
    "Are you ready to start recycling? Let's begin!"
    
    # Important: Loop until explicitly told to return
    while True:
        # Show the screen and capture the result
        $ result = renpy.call_screen("pant_game")
        
        # If the result is "end_game", break the loop and continue to level selection
        if result == "end_game":
            jump level_choose
    
    # We should never reach this point, but just in case
    jump level_choose

# Modify the screen to return values instead of jumping directly
screen pant_game():
    # Add a full screen background
    add "bg pant_machine" at bg_fullscreen
    
    # Game title
    text "Pant Sorting Game" size 40 xalign 0.5 ypos 50
    
    # Game status display
    text "Score: [player_score]" size 30 xalign 0.5 ypos 100
    text "Bottles remaining: [bottles_remaining]" size 30 xalign 0.5 ypos 150
    
    # Results overlay - shows only after game is finished and button is clicked
    if show_results:
        # Semi-transparent overlay with black background for better readability
        frame:
            background "#000c"  # Black background with high opacity
            xfill True
            yfill True
            
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 20
                
                text "Game Complete!" size 50 xalign 0.5 color "#fff" outlines [(2, "#000", 0, 0)]
                
                if player_score >= 10:
                    text "Great job! You earned [player_score] kroner from panting!" color "#fff" xalign 0.5 outlines [(2, "#000", 0, 0)]
                    text "You're a natural at recycling!" color "#fff" xalign 0.5 outlines [(2, "#000", 0, 0)]
                elif player_score >= 5:
                    text "Not bad! You earned [player_score] kroner from panting." color "#fff" xalign 0.5 outlines [(2, "#000", 0, 0)]
                    text "With a bit more practice, you'll be a panting expert!" color "#fff" xalign 0.5 outlines [(2, "#000", 0, 0)]
                else:
                    text "You earned [player_score] kroner from panting." color "#fff" xalign 0.5 outlines [(2, "#000", 0, 0)]
                    text "Keep practicing to learn which bottles are pantable!" color "#fff" xalign 0.5 outlines [(2, "#000", 0, 0)]
                
                text "Thanks for playing the pant sorting game!" color "#fff" xalign 0.5 outlines [(2, "#000", 0, 0)]
                
                # Return "end_game" instead of jumping directly
                textbutton "Return to Level Selection" action Return("end_game") xalign 0.5 xpadding 40 ypadding 20
    
    # Check if game is finished but results not yet shown
    elif game_finished:
        textbutton "See Results" action Function(show_game_results) xalign 0.5 yalign 0.6 xpadding 60 ypadding 30 background "#8888" text_size 36 text_color "#fff"

    # Gameplay elements - only shown when game is still in progress
    else:
        draggroup:
            # Pant zone on the left (droppable)
            drag:
                drag_name "pant_zone"
                xpos 50  # LEFT POSITION
                ypos 360  # VERTICAL POSITION
                draggable False  # This is a drop target, not draggable
                
                frame:
                    xsize 300
                    ysize 200
                    background "pant_zone"
                    
                    text "PANT" size 40 xalign 0.5 yalign 0.5 color "#00ff00"
            
            # Discard zone on the right (droppable)
            drag:
                drag_name "discard_zone"
                xpos 1600  # RIGHT POSITION
                ypos 360   # VERTICAL POSITION
                draggable False  # This is a drop target, not draggable
                
                frame:
                    xsize 300
                    ysize 200
                    background "discard_zone"
                    
                    text "DISCARD" size 40 xalign 0.5 yalign 0.5 color "#ff0000"
        
            # Current bottle as a draggable element
            $ current_bottle = game_bottles[len(game_bottles) - bottles_remaining]
            $ current_image = bottles[current_bottle]["image"]
            
            # The draggable bottle - positioned in the exact center between the two zones
            drag:
                drag_name "bottle"
                xpos 825  # HORIZONTAL POSITION - Centered between 50 and 1600
                ypos 400  # VERTICAL POSITION - Raised from 360 to 400
                drag_handle (0, 0, 350, 350)  # Increased drag handle area
                
                add current_image:
                    at bottle_size
                
                dragged draggable_dropped
        
        # Instructions - moved lower on screen (from 650 to 750)
        text "Drag the bottle to PANT or DISCARD" size 30 xalign 0.5 ypos 750 outlines [(2, "#000", 0, 0)]

# Alternative results screen using NVL style
screen pant_results():
    tag nvl
    
    window:
        style "nvl_window"
        
        vbox:
            spacing gui.nvl_spacing
            
            text "Game Complete!" size 40 xalign 0.5
            
            null height 20
            
            if player_score >= 10:
                text "Great job! You earned [player_score] kroner from panting!"
                text "You're a natural at recycling!"
            elif player_score >= 5:
                text "Not bad! You earned [player_score] kroner from panting."
                text "With a bit more practice, you'll be a panting expert!"
            else:
                text "You earned [player_score] kroner from panting."
                text "Keep practicing to learn which bottles are pantable!"
            
            null height 20
            
            text "Thanks for playing the pant sorting game!"
            
            null height 40
            
            textbutton "Return to Level Selection" action Return("end_game") xalign 0.5 xpadding 40 ypadding 20

# We don't need this label anymore since we handle everything in the main label
label pant_game_result:
    jump level_choose 