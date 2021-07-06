import arcade
from core.action import Action
from game import constants
from core.cue import Cue


class ControlActorsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        cue_info = cue.get_info()
        cue_name = cue.get_name()
        if cue_name == Cue.ON_KEY_PRESS:
            if cue_info["key"] == arcade.key.UP:
                player = cast.first_actor("players")
                player.jump()
            if cue_info["key"] == arcade.key.LEFT:
                player = cast.first_actor("players")
                player.walk(-1 * constants.MOVE_SPEED)
            if cue_info["key"] == arcade.key.RIGHT:
                player = cast.first_actor("players")
                player.walk(constants.MOVE_SPEED)
        elif cue_name == Cue.ON_KEY_RELEASE:
            if cue_info["key"] == arcade.key.LEFT:
                player = cast.first_actor("players")
                player.walk(0)
            if cue_info["key"] == arcade.key.RIGHT:
                player = cast.first_actor("players")
                player.walk(0)