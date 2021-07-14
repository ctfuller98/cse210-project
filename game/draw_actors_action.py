from core.action import Action


class DrawActorsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        cast.get_actors("map")[0].draw()
        self._draw_player(cast)
        self._draw_instructions(cast)
        self._draw_health_bars(cast)

        
        
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
    
    
    #If there's a more elegant way to draw the two healthbars differently, I'd be welcome to hearing it. -Braxton
    def _draw_health_bars(self, cast):
        player = cast.get_actors("players")[0]
        player._draw_health_bar(0)
        player = cast.get_actors("players")[1]
        player._draw_health_bar(1)    
    