import arcade
import os
# GAME CONSTANTS
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 800
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2
GRAVITY = 1
# ANIMAL CONSTANTS
MOVE_SPEED = 6
PLAYER_JUMP_SPEED = 15
PLAYER_ANIMATION_RATE = 7
PROJECT_ROOT = os.path.dirname(__file__)
PLAYER_PATH = os.path.join(PROJECT_ROOT, "assets/KOO")
_ANIMATIONS = {}

def _load_texture(name, filename, path, mirrored=False):
    _ANIMATIONS[name] = {}
    _ANIMATIONS[name][False] = arcade.load_texture(f"{path}/{filename}.png")
    if mirrored:
        _ANIMATIONS[name][True] = arcade.load_texture(f"{path}/{filename}.png", flipped_horizontally=True)

# If mirrorred is true then a mirrored set of sprites is created
def _load_texture_array(name, filename, count, path,  mirrored=False):
    # Create a second dictionary, this stores mirrored and unmirrored sprites
    _ANIMATIONS[name] = {}
    _ANIMATIONS[name][False] = []
    if mirrored:
        _ANIMATIONS[name][True] = []

    for index in range(1, count + 1):
        _ANIMATIONS[name][False].append(arcade.load_texture(f"{path}/{filename}{index}.png"))
        if mirrored:
            # Apparenetly mirrored is deprecated so that's why I'm using flipped_horizontally
            _ANIMATIONS[name][True].append(arcade.load_texture(f"{path}/{filename}{index}.png", flipped_horizontally = True))

def get_texture(name, mirrored=False):
    return _ANIMATIONS[name][mirrored]

#(NAME OF ANIMATION , FILE PATH/FILE NAME, NUMBER OF FILES , MIRRORED?) 

_load_texture_array("PLAYER_FALLING", "Fall/Fall", 2, PLAYER_PATH,  True)

_load_texture_array("PLAYER_IDLE", "Idle/Idle", 8, PLAYER_PATH, True)
#JUMPING
_load_texture("PLAYER_JUMPING", "Jump/Jump2", PLAYER_PATH, True)
#WALKING
_load_texture_array("PLAYER_WALKING", "Run/Run",  8, PLAYER_PATH, True)

#FALLING
_load_texture_array("PLAYER_FALLING", "Fall/Fall", 2, PLAYER_PATH, True)
#ATTACK 1
_load_texture_array("ATTACK_ONE", "Attack1/Attack1.", 4, PLAYER_PATH, True)
#ATTACK 2 
_load_texture_array("ATTACK_TWO", "Attack2/Attack2.", 4, PLAYER_PATH, True)


# GROUND CONSTANTS

GROUND_MOVE_SPEED = -8
GROUND_PATH = ":resources:images/tiles"
GROUND_GRASS = arcade.load_texture(f"{GROUND_PATH}/grass.png")

# HEALTH CONSTANTS

HEALTHBAR_WIDTH = 25
HEALTHBAR_HEIGHT = 3
HEALTHBAR_OFFSET_Y = -10