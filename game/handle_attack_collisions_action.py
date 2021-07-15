from game import constants
from core.action import Action
import arcade

class HandleAttackCollisionsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        self._handle_attack_collisions(cast)

    def _handle_attack_collisions(self, cast):
        player1 = cast.get_actors("players")[0]
        player2 = cast.get_actors("players")[1]
        if arcade.check_for_collision(player1, player2):

            if(player1.is_hitting()):
                if player2.blocking(player1):
                    player2.block()
                else:
                    player2.damage(constants.DEFAULT_ATTACK_DAMAGE)
                
        
            if(player2.is_hitting()):
                if player1.blocking(player2):
                    player1.block()
                else:
                    player1.damage(constants.DEFAULT_ATTACK_DAMAGE)
         