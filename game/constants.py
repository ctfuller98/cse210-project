import arcade
import os
# GAME CONSTANTS
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2
GRAVITY = 1
# SPRITE CONSTANTS
PLAYER_JUMP_SPEED = 15
PLAYER_ANIMATION_RATE = 3
PROJECT_ROOT = os.path.dirname(__file__)
PLAYER_PATH = os.path.join(PROJECT_ROOT, "assets/KOO/Sprites")

#IDLE
PLAYER_IDLE = [None] * 8
PLAYER_IDLE[0] = arcade.load_texture(f"{PLAYER_PATH}/Idle/Idle1.png")
PLAYER_IDLE[1] = arcade.load_texture(f"{PLAYER_PATH}/Idle/Idle2.png")
PLAYER_IDLE[2] = arcade.load_texture(f"{PLAYER_PATH}/Idle/Idle3.png")
PLAYER_IDLE[3] = arcade.load_texture(f"{PLAYER_PATH}/Idle/Idle4.png")
PLAYER_IDLE[4] = arcade.load_texture(f"{PLAYER_PATH}/Idle/Idle5.png")
PLAYER_IDLE[5] = arcade.load_texture(f"{PLAYER_PATH}/Idle/Idle6.png")
PLAYER_IDLE[6] = arcade.load_texture(f"{PLAYER_PATH}/Idle/Idle7.png")
PLAYER_IDLE[7] = arcade.load_texture(f"{PLAYER_PATH}/Idle/Idle8.png")

#JUMPING
PLAYER_JUMPING = [None] * 2
PLAYER_JUMPING[0] = arcade.load_texture(f"{PLAYER_PATH}/Jump/Jump1.png")
PLAYER_JUMPING[1] = arcade.load_texture(f"{PLAYER_PATH}/Jump/Jump2.png")
PLAYER_WALKING = [None] * 8 
PLAYER_WALKING[0] = arcade.load_texture(f"{PLAYER_PATH}/Run/Run1.png")
PLAYER_WALKING[1] = arcade.load_texture(f"{PLAYER_PATH}/Run/Run2.png")
PLAYER_WALKING[2] = arcade.load_texture(f"{PLAYER_PATH}/Run/Run3.png")
PLAYER_WALKING[3] = arcade.load_texture(f"{PLAYER_PATH}/Run/Run4.png")
PLAYER_WALKING[4] = arcade.load_texture(f"{PLAYER_PATH}/Run/Run5.png")
PLAYER_WALKING[5] = arcade.load_texture(f"{PLAYER_PATH}/Run/Run6.png")
PLAYER_WALKING[6] = arcade.load_texture(f"{PLAYER_PATH}/Run/Run7.png")
PLAYER_WALKING[7] = arcade.load_texture(f"{PLAYER_PATH}/Run/Run8.png")

#FALLING
PLAYER_FALLING = [None] * 2 
PLAYER_FALLING[0] = arcade.load_texture(f"{PLAYER_PATH}/Fall/Fall1.png")
PLAYER_FALLING[1] = arcade.load_texture(f"{PLAYER_PATH}/Fall/Fall2.png")

#ATTACK 1 
ATTACK1 = [None]*4
ATTACK1[0] = arcade.load_texture(f"{PLAYER_PATH}/Attack1/Attack1.1.png")
ATTACK1[1] = arcade.load_texture(f"{PLAYER_PATH}/Attack1/Attack1.2.png")
ATTACK1[2] = arcade.load_texture(f"{PLAYER_PATH}/Attack1/Attack1.3.png")
ATTACK1[3] = arcade.load_texture(f"{PLAYER_PATH}/Attack1/Attack1.4.png")

#ATTACK 2 
ATTACK2 = [None]*4
ATTACK2[0] = arcade.load_texture(f"{PLAYER_PATH}/Attack2/Attack2.1.png")
ATTACK2[1] = arcade.load_texture(f"{PLAYER_PATH}/Attack2/Attack2.2.png")
ATTACK2[2] = arcade.load_texture(f"{PLAYER_PATH}/Attack2/Attack2.3.png")
ATTACK2[3] = arcade.load_texture(f"{PLAYER_PATH}/Attack2/Attack2.4.png")


# GROUND CONSTANTS

GROUND_MOVE_SPEED = -8
GROUND_PATH = ":resources:images/tiles"
GROUND_GRASS = arcade.load_texture(f"{GROUND_PATH}/grass.png")