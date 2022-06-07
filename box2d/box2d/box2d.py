"""
 BOX 2D Engine 

 Author: Jason Knoll

 The BOX 2D engine is a simple 2 dimensional fighting
 game engine based off the 'Arcade' 2D game development
 library. I know nothing of game development and I'm 
 doing this for fun.

 This file should serve as the main file for the engine.
"""

# Imports
import arcade as a

# Constants
version = '0.0.2'
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
SCREEN_TITLE = f"BOX 2D Engine v{version}"


class MainMenu(a.Window):
    """Main menu window
    """

    def __init__(self):
        """Initialize the window
        """

        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the background window
        a.set_background_color(a.color.ASH_GREY)

    def on_draw(self):
        """Called whenever you need to draw your window
        """

        # Clear the screen and start drawing
        a.start_render()

        # Draw a blue circle
        a.draw_circle_filled(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 15, a.color.BLUE
        )


# Main code entry point
if __name__ == "__main__":
    app = MainMenu()
    a.run()
