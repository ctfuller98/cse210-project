class Cue:

    ON_DRAW = "ON_DRAW"
    ON_KEY_PRESS = "ON_KEY_PRESS"
    ON_KEY_RELEASE = "ON_KEY_RELEASE"
    ON_MOUSE_DRAG = "ON_MOUSE_DRAG"
    ON_MOUSE_MOTION = "ON_MOUSE_MOTION"
    ON_MOUSE_PRESS = "ON_MOUSE_PRESS"
    ON_MOUSE_RELEASE = "ON_MOUSE_RELEASE"
    ON_MOUSE_SCROLL = "ON_MOUSE_SCROLL"
    ON_UPDATE = "ON_UPDATE"

    def __init__(self, name, info):
        self._name = name
        self._info = info

    def get_info(self):
        return self._info
    
    def get_name(self):
        return self._name

    