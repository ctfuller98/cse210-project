import arcade
from arcade.key import A
from core.action import Action
from game import constants
from core.cue import Cue


class ControlActorsAction(Action):
    
    def __init__(self):
        super().__init__()
        self.input_1 = {"x":0}
        self.input_2 = {"x":0}

    def execute(self, cast, cue, callback):
        cue_info = cue.get_info()
        cue_name = cue.get_name()
        self.update_player(cue, cast.get_actors("players")[0], {
            "jump" : arcade.key.W,
            "left" : arcade.key.A,
            "right" : arcade.key.D,
            "attack_up" : arcade.key.Z,
            "attack_forward" : arcade.key.X,
            "attack_down" : arcade.key.C
        }, self.input_1)
        self.update_player(cue, cast.get_actors("players")[1], {
            "jump" : arcade.key.I,
            "left" : arcade.key.J,
            "right" : arcade.key.L,
            "attack_up" : arcade.key.M,
            "attack_forward" : arcade.key.COMMA,
            "attack_down" : arcade.key.PERIOD
        }, self.input_2)
        

    def update_player(self, cue, player, keyset, persistant_data):
        cue_info = cue.get_info()
        cue_name = cue.get_name()
        if cue_name == Cue.ON_KEY_PRESS:
            if cue_info["key"] == keyset["jump"]:
                player.jump()
            if cue_info["key"] == keyset["left"]:
                persistant_data["x"] -= 1
            if cue_info["key"] == keyset["right"]:
                persistant_data["x"] += 1
            if cue_info["key"] == keyset["attack_up"]:
                player.attack_up(True)
            if cue_info["key"] == keyset["attack_forward"]:
                player.attack_forward(True)
            if cue_info["key"] == keyset["attack_down"]:
                player.attack_down(True)
            
            player.walk(persistant_data["x"] * constants.MOVE_SPEED)
        elif cue_name == Cue.ON_KEY_RELEASE:
            if cue_info["key"] == keyset["left"]:
                persistant_data["x"] += 1
            if cue_info["key"] == keyset["right"]:
                persistant_data["x"] -= 1
            player.walk(persistant_data["x"] * constants.MOVE_SPEED)
