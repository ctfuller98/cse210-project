class Action:

    class Callback:

        def on_finished(self, next_scene):
            pass

    def __init__(self):
        self._enabled = True

    def enable(self):
        self._enable = True

    def disable(self):
        self._enable = False
        
    def execute(self, cast, cue, callback):
        pass
    
    def is_enabled(self):
        return self._enabled