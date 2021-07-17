import arcade
from core.director import Director
from game import constants
import game
from game.game_scene import GameScene


def main():
    width = constants.SCREEN_WIDTH
    height = constants.SCREEN_HEIGHT
    game_scene = GameScene()
    game_scene.play_music()
    director = Director(width, height)
    director.direct_scene(game_scene)
    arcade.run()


if __name__ == "__main__":
    main()