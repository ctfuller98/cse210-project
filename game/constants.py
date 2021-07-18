import arcade
import os
from arcade import sound
import random
# GAME CONSTANTS
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000
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
#=================SOUND CONSTANTS==============================#
def get_sound(spriteindex, name):
    if spriteindex == 0:
        JUMP = sound.load_sound(os.path.join(PLAYER_SOUND, "Jump.mp3"))
        UP = sound.load_sound(os.path.join(PLAYER_SOUND, "Strike1.1.wav"))
        DOWN = sound.load_sound(os.path.join(PLAYER_SOUND, "Strike1.2.wav"))
        SIDE = sound.load_sound(os.path.join(PLAYER_SOUND, "Strike1.3.wav"))
        HIT_ONE = sound.load_sound(os.path.join(PLAYER_SOUND, "Hit1.1.wav"))
        HIT_TWO = sound.load_sound(os.path.join(PLAYER_SOUND, "Hit1.2.wav"))
        HIT_THREE = sound.load_sound(os.path.join(PLAYER_SOUND, "Hit1.3.wav"))
        HITS = [HIT_ONE, HIT_TWO, HIT_THREE]
        if name == "JUMP":
            return JUMP
        elif name == "UP":
            return UP
        elif name == "DOWN":
            return DOWN
        elif name == "SIDE":
            return SIDE
        elif name == "HIT":
            return random.choice(HITS)
    elif spriteindex == 1: 
        JUMP = sound.load_sound(os.path.join(PLAYER_TWO_SOUND, "Jump.mp3"))
        UP = sound.load_sound(os.path.join(PLAYER_TWO_SOUND, "Strike1.1.wav"))
        DOWN = sound.load_sound(os.path.join(PLAYER_TWO_SOUND, "Strike1.2.wav"))
        SIDE = sound.load_sound(os.path.join(PLAYER_TWO_SOUND, "Strike1.3.wav"))
        HIT_ONE = sound.load_sound(os.path.join(PLAYER_TWO_SOUND, "Hit1.1.wav"))
        HIT_TWO = sound.load_sound(os.path.join(PLAYER_TWO_SOUND, "Hit1.2.wav"))
        HIT_THREE = sound.load_sound(os.path.join(PLAYER_TWO_SOUND, "Hit1.3.wav"))
        HITS = [HIT_ONE, HIT_TWO, HIT_THREE]
        if name == "JUMP":
            return JUMP
        elif name == "UP":
            return UP
        elif name == "DOWN":
            return DOWN
        elif name == "SIDE":
            return SIDE
        elif name == "HIT":
            return random.choice(HITS)

#===========================BACKGROUND MUSIC CONSTANTS=======================#
MUSIC_VOLUME = 0.5
SONG_1 = MUSIC_PATH + "\Battle.mp3"
SONG_2 = MUSIC_PATH + "\Epic Drums.mp3"
SONG_3 = MUSIC_PATH + "\Action Fight.mp3"
SONG_4 = MUSIC_PATH + "\Action Rhythms.mp3"
SONG_5 = MUSIC_PATH + "\Daredevil.mp3"
SONG_6 = MUSIC_PATH + "\Last Time.mp3"
MUSIC_LIST = [SONG_1, SONG_2, SONG_3, SONG_4, SONG_5, SONG_6]

#(NAME OF ANIMATION , FILE PATH/FILE NAME, NUMBER OF FILES , MIRRORED?) 

#----------------------------PLAYER ONE-----------------------------#
#IDLE
_load_texture_array(0, "PLAYER_FALLING", "Fall/Fall", 2, PLAYER_PATH)
_load_texture_array(0, "PLAYER_IDLE", "Idle/Idle", 8, PLAYER_PATH, True)
#JUMPING
_load_texture(0, "PLAYER_JUMPING", "Jump/Jump2", PLAYER_PATH, True)
#WALKING
_load_texture_array(0, "PLAYER_WALKING", "Run/Run",  8, PLAYER_PATH, True)

#DEATH
_load_texture_array(0, "PLAYER_DEATH", "Death/Death",  6, PLAYER_PATH, True)
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
#DEATH
_load_texture_array(1, "PLAYER_DEATH", "Death/Death",  10, PLAYER_PATH_TWO, True)
#FALLING
_load_texture_array(1, "PLAYER_FALLING", "Fall/Fall", 2, PLAYER_PATH_TWO, True)
#SIDE ATTACK
_load_texture_array(1, "ATTACK_ONE", "Attack1/Attack1.", 7, PLAYER_PATH_TWO, True)
#UP ATTACK
_load_texture_array(1, "ATTACK_TWO", "Attack2/Attack2.", 6, PLAYER_PATH_TWO, True)
#DOWN ATTACK
_load_texture_array(1, "ATTACK_THREE", "Attack3/Attack3.", 7, PLAYER_PATH_TWO, True)


# HEALTH CONSTANTS

HEALTHBAR_WIDTH = 50
HEALTHBAR_HEIGHT = 6

# ATTACK CONSTANTS

# Attack time, how long any move will take to hit
ATTACK_TIME = 20
DEFAULT_ATTACK_DAMAGE = 25
ATTACK_FRAME = {
    "ATTACK_ONE" : [2,6],
    "ATTACK_TWO" : [2,3],
    "ATTACK_THREE" : [2,4],
}
