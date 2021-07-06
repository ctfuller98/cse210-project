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


class GameScene(Scene):

    def __init__(self):
        
        # create the cast
        player = Player()
        cast = Cast()
        cast.add_actor("players", player)

        for i in range(10):
            ground = Ground()
            ground.left = (i * ground.width)
            cast.add_actor("grounds", ground)
        
        instruction = Instruction()
        cast.add_actor("instructions", instruction)

        # create the script
        control_actors_action = ControlActorsAction()
        move_actors_action = MoveActorsAction()
        handle_collisions_action = HandleCollisionsAction()
        draw_actors_action = DrawActorsAction()

        script = Script()
        script.add_action(Cue.ON_KEY_PRESS, control_actors_action)
        script.add_action(Cue.ON_UPDATE, move_actors_action)
        script.add_action(Cue.ON_UPDATE, handle_collisions_action)
        script.add_action(Cue.ON_DRAW, draw_actors_action)
        
        # set the scene
        self.set_cast(cast)
        self.set_script(script)