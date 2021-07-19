from game import handle_attack_collisions_action
from core.cast import Cast
from core.cue import Cue
from core.scene import Scene
from core.script import Script
from game.player import Player
from game.ground import Ground
from game.instructions import Instruction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_attack_collisions_action import HandleAttackCollisionsAction
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.move_actors_action import MoveActorsAction
from game.check_win_action import CheckWinAction
from game.map import Map
from game import constants
import arcade
import random

class GameScene(Scene):

    def __init__(self):
        
        # create the cast
        player1 = Player(100, 0, False)
        player2 = Player(700, 1, True)
        cast = Cast()
        cast.add_actor("players", player1)
        cast.add_actor("players", player2)
        
        #instruction = Instruction()
        #cast.add_actor("instructions", instruction)

  # create the script
        self.control_actors_action = ControlActorsAction()
        self.move_actors_action = MoveActorsAction()
        self.handle_collisions_action = HandleCollisionsAction()
        self.handle_attack_collisions_action = HandleAttackCollisionsAction()
        self.draw_actors_action = DrawActorsAction()
        self.check_win_action = CheckWinAction(self)

        script = Script()
        script.add_action(Cue.ON_KEY_PRESS, self.control_actors_action)
        script.add_action(Cue.ON_KEY_RELEASE, self.control_actors_action)
        script.add_action(Cue.ON_UPDATE, self.move_actors_action)
        script.add_action(Cue.ON_UPDATE, self.handle_collisions_action)
        script.add_action(Cue.ON_UPDATE, self.handle_attack_collisions_action)
        script.add_action(Cue.ON_DRAW, self.draw_actors_action)
        script.add_action(Cue.ON_UPDATE, self.check_win_action)
        # set the scene
        self.set_cast(cast)
        self.set_script(script)
        script.remove_action
        self.map_name = "game/assets/maps/dev_blocks.tmx"
        self._map = Map(self.map_name, self)

    def player_won(self, player_index):
        script = self.get_script()
        script.remove_action(Cue.ON_UPDATE, self.handle_attack_collisions_action)
        script.remove_action(Cue.ON_KEY_PRESS, self.control_actors_action)
        script.remove_action(Cue.ON_KEY_RELEASE, self.control_actors_action)
        script.remove_action(Cue.ON_UPDATE, self.check_win_action)

        print(f"player {player_index} won!")
        script.clean_actions()
        # Win stuff here
        # script.add_action(Cue.ON_KEY_PRESS, check_for_next_scene_action)
        
    def play_music(self):
            self.enable_bg_music = True
            self.music_list = constants.MUSIC_LIST
            if self.enable_bg_music:
                songs = self.music_list
                bg_song = random.choice(songs)
                self.background_music = arcade.load_sound(bg_song)
                arcade.play_sound(self.background_music)