from arcade.key import SPACE
from core.action import Action
import arcade

class CheckForNextSceneAction(Action):
    def __init__(self, next_scene):
        self._next_scene = next_scene
        super().__init__()

    def execute(self, cast, cue, callback):
        cue_info = cue.get_info()
        cue_name = cue.get_name()
        if cue_info["key"] == arcade.key.SPACE:
            callback.direct_scene(self._next_scene)