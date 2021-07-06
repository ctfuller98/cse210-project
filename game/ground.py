from core.actor import Actor
from game import constants


class Ground(Actor):

    def __init__(self):
        super().__init__()
        self.texture = constants.GROUND_GRASS
        self.scale = 0.75
        self.center_x = 0 + (self.width / 2)
        self.center_y = 0 + (self.height / 2)
        self.change_x = 0
        
        
    def update(self):
        self.center_x += self.change_x