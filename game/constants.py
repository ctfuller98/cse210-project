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
PLAYER_SOUND = os.path.join(PROJECT_ROOT, "assets/KOO/Sounds")
PLAYER_TWO_SOUND = os.path.join(PROJECT_ROOT, "assets/SING/Sounds")
PLAYER_PATH = os.path.join(PROJECT_ROOT, "assets/KOO")
PLAYER_PATH_TWO = os.path.join(PROJECT_ROOT, "assets/SING")
MUSIC_PATH = os.path.join(PROJECT_ROOT, "assets/Bkgmusic")
_ANIMATIONS = [{}, {}]
def _load_texture(spriteindex, name, filename, path, mirrored=False):
    _ANIMATIONS[spriteindex][name] = {}
    _ANIMATIONS[spriteindex][name][False] = arcade.load_texture(f"{path}/{filename}.png")
    if mirrored:
        _ANIMATIONS[spriteindex][name][True] = arcade.load_texture(f"{path}/{filename}.png", flipped_horizontally=True)

# If mirrorred is true then a mirrored set of sprites is created
def _load_texture_array(spriteindex, name, filename, count, path,  mirrored=False):
    # Create a second dictionary, this stores mirrored and unmirrored sprites
    _ANIMATIONS[spriteindex][name] = {}
    _ANIMATIONS[spriteindex][name][False] = []
    if mirrored:
        _ANIMATIONS[spriteindex][name][True] = []

    for index in range(1, count + 1):
        _ANIMATIONS[spriteindex][name][False].append(arcade.load_texture(f"{path}/{filename}{index}.png"))
        if mirrored:
            # Apparenetly mirrored is deprecated so that's why I'm using flipped_horizontally
            _ANIMATIONS[spriteindex][name][True].append(arcade.load_texture(f"{path}/{filename}{index}.png", flipped_horizontally = True))

def get_texture(spriteindex, name, mirrored=False):
    return _ANIMATIONS[spriteindex][name][mirrored]

#(NAME OF ANIMATION , FILE PATH/FILE NAME, NUMBER OF FILES , MIRRORED?) 

#----------------------------PLAYER ONE-----------------------------#
#IDLE
_load_texture_array(0, "PLAYER_IDLE", "Idle/Idle", 8, PLAYER_PATH, True)
#JUMPING
_load_texture(0, "PLAYER_JUMPING", "Jump/Jump2", PLAYER_PATH, True)
#WALKING
_load_texture_array(0, "PLAYER_WALKING", "Run/Run",  8, PLAYER_PATH, True)
#FALLING
_load_texture_array(0, "PLAYER_FALLING", "Fall/Fall", 2, PLAYER_PATH, True)
#SIDE ATTACK
_load_texture_array(0, "ATTACK_ONE", "Attack1/Attack1.", 4, PLAYER_PATH, True)
#UP ATTACK
_load_texture_array(0, "ATTACK_TWO", "Attack2/Attack2.", 4, PLAYER_PATH, True)
#DOWN ATTACK
_load_texture_array(0, "ATTACK_THREE", "Attack3/Attack3.", 4, PLAYER_PATH, True)

#---------------------------PLAYER TWO------------------------------------#
#FALL
_load_texture_array(1, "PLAYER_FALLING", "Fall/Fall", 2, PLAYER_PATH_TWO)
#IDLE
_load_texture_array(1, "PLAYER_IDLE", "Idle/Idle", 8, PLAYER_PATH_TWO, True)
#JUMPING
_load_texture(1, "PLAYER_JUMPING", "Jump/Jump2", PLAYER_PATH_TWO, True)
#WALKING
_load_texture_array(1, "PLAYER_WALKING", "Run/Run",  8, PLAYER_PATH_TWO, True)
#FALLING
_load_texture_array(1, "PLAYER_FALLING", "Fall/Fall", 2, PLAYER_PATH_TWO, True)
#SIDE ATTACK
_load_texture_array(1, "ATTACK_ONE", "Attack1/Attack1.", 7, PLAYER_PATH_TWO, True)
#UP ATTACK
_load_texture_array(1, "ATTACK_TWO", "Attack2/Attack2.", 6, PLAYER_PATH_TWO, True)
#DOWN ATTACK
_load_texture_array(1, "ATTACK_THREE", "Attack3/Attack3.", 7, PLAYER_PATH_TWO, True)

#-------------------------GROUND CONSTANTS---------------------------#

GROUND_MOVE_SPEED = -8
GROUND_PATH = ":resources:images/tiles"
GROUND_GRASS = arcade.load_texture(f"{GROUND_PATH}/grass.png")

# HEALTH CONSTANTS

HEALTHBAR_WIDTH = 50
HEALTHBAR_HEIGHT = 6

# ATTACK CONSTANTS

DEFAULT_ATTACK_DAMAGE = 25
ATTACK_FRAME = {
    "ATTACK_ONE" : [2,6],
    "ATTACK_TWO" : [2,3], # Needs to be set
    "ATTACK_THREE" : [2,6], # Needs to be set
}
