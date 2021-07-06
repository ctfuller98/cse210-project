from core.action import Action


class DrawActorsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        self._draw_player(cast)
        self._draw_ground(cast)
        self._draw_instructions(cast)
        
    def _draw_ground(self, cast):
        grounds = cast.get_actors("grounds")
        for ground in grounds:
            ground.draw()
    
    def _draw_instructions(self, cast):
        instructions = cast.get_actors("instructions")
        for instruction in instructions:
            instruction.draw()
    
    def _draw_player(self, cast):
        players = cast.get_actors("players")
        for player in players:
            player.draw()
    