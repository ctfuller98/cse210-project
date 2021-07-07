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
            player = cast.get_actors("players")[0]
            if cue_info["key"] == arcade.key.UP:
                player.jump()
            if cue_info["key"] == arcade.key.LEFT:
                player.walk(-1 * constants.MOVE_SPEED)
            if cue_info["key"] == arcade.key.RIGHT:
                player.walk(constants.MOVE_SPEED)

            player = cast.get_actors("players")[1]
            if cue_info["key"] == arcade.key.W:
                player.jump()
            if cue_info["key"] == arcade.key.A:
                player.walk(-1 * constants.MOVE_SPEED)
            if cue_info["key"] == arcade.key.D:
                player.walk(constants.MOVE_SPEED)
        elif cue_name == Cue.ON_KEY_RELEASE:
            player = cast.first_actor("players")
            if cue_info["key"] == arcade.key.LEFT:
                player.walk(0)
            if cue_info["key"] == arcade.key.RIGHT:
                player.walk(0)

            player = cast.get_actors("players")[1]
            if cue_info["key"] == arcade.key.A:
                player.walk(0)
            if cue_info["key"] == arcade.key.D:
                player.walk(0)
