      #----------------------------------------------------------------------------
      # Created By  :       
      # Created Date:       
      # Project Name:       
      # Project Purpose:    
      # Project Function:   
      # ---------------------------------------------------------------------------
      # Psuedocode:
      # 
      # ---------------------------------------------------------------------------
from ursina import *                    # Import the ursina engine
from ursina.prefabs.platformer_controller_2d import PlatformerController2d 
app = Ursina()                          # Initialise your Ursina app

window.title = 'My Game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter
player = PlatformerController2d(y=1, z=.01, scale_y=1, max_jumps=2)
ground = Entity(model='quad', scale_x = 10, y=-3 , collider='box', color=color.yellow)



app.run() 