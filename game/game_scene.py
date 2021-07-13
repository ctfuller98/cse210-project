from game import handle_attack_collisions_action
from core.cast import Cast
from core.cue import Cue
from core.scene import Scene
from core.script import Script
from game.player import Player
from game.ground import Ground
from game.instructions import Instruction
from game.handle_collisions_action import HandleCollisionsAction
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.move_actors_action import MoveActorsAction
from game.map import Map

class GameScene(Scene):

    def __init__(self):
        
        # create the cast
        player1 = Player(100, 0, False)
        player2 = Player(700, 1, True)

        cast = Cast()
        cast.add_actor("players", player1)
        cast.add_actor("players", player2)
        
        instruction = Instruction()
        cast.add_actor("instructions", instruction)

  # create the script
        control_actors_action = ControlActorsAction()
        move_actors_action = MoveActorsAction()
        handle_collisions_action = HandleCollisionsAction()
        draw_actors_action = DrawActorsAction()

        script = Script()
        script.add_action(Cue.ON_KEY_PRESS, control_actors_action)
        script.add_action(Cue.ON_KEY_RELEASE, control_actors_action)
        script.add_action(Cue.ON_UPDATE, move_actors_action)
        script.add_action(Cue.ON_UPDATE, handle_collisions_action)
        script.add_action(Cue.ON_DRAW, draw_actors_action)
        
        # set the scene
        self.set_cast(cast)
        self.set_script(script)

        self.map_name = "game/assets/maps/dev_blocks.tmx"
        self._map = Map(self.map_name, self)
