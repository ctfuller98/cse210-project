from core.action import Action

class CheckWinAction(Action):
    
    def __init__(self, scene):
        super().__init__()
        self._scene = scene

    def execute(self, cast, cue, callback):
        players = cast.get_actors("players")
        for playerIndex in range(len(players)):
            player = players[playerIndex]
            if player.is_dead():
                self._scene.player_won(playerIndex)