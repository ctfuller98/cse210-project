import arcade
from arcade.key import A
from core.action import Action
from game import constants
from core.cue import Cue


class ControlActorsAction(Action):
    
    def __init__(self):
        super().__init__()
        self.input_x1 = 0
        self.input_x2 = 0

    def execute(self, cast, cue, callback):
        cue_info = cue.get_info()
        cue_name = cue.get_name()
        if cue_name == Cue.ON_KEY_PRESS:
            player = cast.get_actors("players")[0]
            if cue_info["key"] == arcade.key.UP:
                player.jump()
            if cue_info["key"] == arcade.key.LEFT:
                self.input_x1 -= 1
            if cue_info["key"] == arcade.key.RIGHT:
                self.input_x1 += 1
            player.walk(self.input_x1 * constants.MOVE_SPEED)

            player = cast.get_actors("players")[1]
            if cue_info["key"] == arcade.key.W:
                player.jump()
            if cue_info["key"] == arcade.key.A:
                self.input_x2 -= 1
            if cue_info["key"] == arcade.key.D:
                self.input_x2 += 1
            player.walk(self.input_x2 * constants.MOVE_SPEED)

            if cue_info["key"] == arcade.key.NUM_1:
                player = cast.first_actor("players")
                player.attack_one(True)
        elif cue_name == Cue.ON_KEY_RELEASE:
            player = cast.first_actor("players")
            if cue_info["key"] == arcade.key.LEFT:
                self.input_x1 += 1
            if cue_info["key"] == arcade.key.RIGHT:
                self.input_x1 -= 1
            player.walk(self.input_x1 * constants.MOVE_SPEED)

            player = cast.get_actors("players")[1]
            if cue_info["key"] == arcade.key.A:
                self.input_x2 += 1
            if cue_info["key"] == arcade.key.D:
                self.input_x2 -= 1
            player.walk(self.input_x2 * constants.MOVE_SPEED)
