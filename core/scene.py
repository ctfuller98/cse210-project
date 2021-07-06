class Scene:

    def __init__(self):
        self._cast = None
        self._script = None

    def get_cast(self):
        return self._cast

    def get_script(self):
        return self._script
  
    def set_cast(self, cast):
        self._cast = cast

    def set_script(self, script):
        self._script = script
    
    