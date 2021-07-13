from core.action import Action
import arcade

class HandleCollisionsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        self._handle_ground_collisions(cast)

    def _handle_ground_collisions(self, cast):
        players = cast.get_actors("players")
        for player in players:
            grounds = cast.get_actors("grounds")
            for ground in grounds:
                if arcade.check_for_collision(player, ground):
                    if abs(player.top - ground.bottom) <= 4:
                        player.change_y = 0
                    elif player.top > ground.top:
                        player.bottom = ground.top
                    player.idle()    