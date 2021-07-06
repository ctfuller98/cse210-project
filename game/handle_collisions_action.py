from core.action import Action
import arcade

class HandleCollisionsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        self._handle_ground_collisions(cast)

    def _handle_ground_collisions(self, cast):
        player = cast.first_actor("players")
        grounds = cast.get_actors("grounds")
        for ground in grounds:
            if arcade.check_for_collision(player, ground):
                player.bottom = ground.top
                player.walk()    