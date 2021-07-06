import arcade
from core.actor import Actor
from game import constants

class Instruction(Actor):

    def __init__(self):
        super().__init__()
     
    def draw(self):
        start_x = constants.CENTER_X
        start_y = constants.SCREEN_HEIGHT - 50
        arcade.draw_text("Press 'SPACE' to jump!", start_x, start_y, 
            arcade.color.WHITE, 12, anchor_x="center")
