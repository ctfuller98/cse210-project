from core.action import Action


class MoveActorsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        self._move_player(cast)
        self._move_ground(cast)
        self._recycle_ground(cast)
        
    def _move_player(self, cast):
        player = cast.first_actor("players")
        player.update()

    def _move_ground(self, cast):
        grounds = cast.get_actors("grounds")
        for ground in grounds:
            ground.update()
        
    def _recycle_ground(self, cast):
        grounds = cast.get_actors("grounds")
        if grounds[0].right < 0:
            ground = grounds.pop(0)
            ground.left = grounds[-1].right
            grounds.append(ground)