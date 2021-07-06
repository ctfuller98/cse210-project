import arcade
from core.action import Action
from core.cue import Cue


class Director(arcade.Window, Action.Callback):
    
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self._scene = None
        
    def direct_scene(self, scene):
        self._scene = scene
    
    def on_draw(self):
        arcade.start_render()
        self._cue_action(Cue.ON_DRAW, {})
        
    def on_key_press(self, key, modifiers):
        cue_info = { "key": key, "modifiers": modifiers }
        self._cue_action(Cue.ON_KEY_PRESS, cue_info)
            
    def on_key_release(self, key, modifiers):
        cue_info = { "key": key, "modifiers": modifiers }
        self._cue_action(Cue.ON_KEY_RELEASE, cue_info)
        
    def on_mouse_drag(self, x, y, dx, dy, buttons, _):
        cue_info = { "x": x, "y": y, "dx": dx, "dy": dy, "buttons": buttons }
        self._cue_action(Cue.ON_MOUSE_DRAG, cue_info)
        
    def on_mouse_motion(self, x, y, dx, dy):
        cue_info = { "x": x, "y": y, "dx": dx, "dy": dy }
        self._cue_action(Cue.ON_MOUSE_MOTION, cue_info)
        
    def on_mouse_press(self, x, y, button, _):
        cue_info = { "x": x, "y": y, "button": button }
        self._cue_action(Cue.ON_MOUSE_PRESS, cue_info)
        
    def on_mouse_release(self, x, y, button, _):
        cue_info = { "x": x, "y": y, "button": button }
        self._cue_action(Cue.ON_MOUSE_RELEASE, cue_info)
        
    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        cue_info = {"x": x, "y": y, "scroll_x": scroll_x, "scroll_y": scroll_y}
        self._cue_action(Cue.ON_MOUSE_SCROLL, cue_info)
        
    def on_scene_finished(self, next_scene):
        self._scene = next_scene

    def on_update(self, delta_time):
        cue_info = { "delta_time": delta_time }
        self._cue_action(Cue.ON_UPDATE, cue_info)
        
    def _cue_action(self, cue_name, cue_info):
        cast = self._scene.get_cast()
        script = self._scene.get_script()
        cue = Cue(cue_name, cue_info)
        for action in script.get_actions(cue_name):
            if action.is_enabled():
                action.execute(cast, cue, self)