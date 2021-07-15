from core.action import Action
import arcade

class HandleCollisionsAction(Action):
    
    def __init__(self):
        super().__init__()
        self.physics_engine_01 = None
        self.physics_engine_02 = None

    def execute(self, cast, cue, callback):
        self._handle_ground_collisions(cast)
        

    def _handle_ground_collisions(self, cast):
        if (self.physics_engine_01 == None):
            self.physics_engine_01 = arcade.PhysicsEngineSimple(cast.get_actors("players")[0], cast._walls)
            self.physics_engine_02 = arcade.PhysicsEngineSimple(cast.get_actors("players")[1], cast._walls)

        self.physics_engine_01.update()
        self.physics_engine_02.update()