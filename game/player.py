from core.actor import Actor
from game import constants
import arcade

class Player(Actor):

    def __init__(self):
        super().__init__()
        self.center_x = constants.CENTER_X
        self.center_y = constants.CENTER_Y
        self._is_jumping = False
        self._is_walking = False
        self._is_attacking = False
        self._current_frame = 0
        self._texture_index = 0
        self.texture = constants.get_texture("PLAYER_IDLE")[0]
        self.scale = 3
        self.facing_left = True
        self.max_health = 100
        self.current_health = 100
        
    def jump(self):
        if not self._is_jumping:
            self._is_jumping = True
            self._is_walking = False
            self.change_y = constants.PLAYER_JUMP_SPEED
    
    def idle(self):
        self._is_jumping = False
        self.change_y = 0
    
    def walk(self, speed):
        self._is_walking = True
        self.change_x = speed
        if(speed != 0):
            self.facing_left = speed < 0

    def attack_one(self,attacking):
        if self._is_jumping == False and self._is_walking == False:
            self._is_attacking = attacking
        else:
            self._is_attacking = False

    def update(self):
        self._update_position()
        self._check_idle()
        self._check_jumping()
        self._check_walking()
        self._check_falling()
        self._check_attacking()
        self._draw_health_bar()
        
    def _check_falling(self):
        if self.change_y < -1:
            num_textures = len(constants.get_texture("PLAYER_FALLING"))
            self._current_frame = 0
            self._texture_index = (self._texture_index + 1) % num_textures
            self.texture = constants.get_texture("PLAYER_FALLING", self.facing_left)[self._texture_index]

    def _check_jumping(self):
        if self.change_y > 0:
            self.texture = constants.get_texture("PLAYER_JUMPING", self.facing_left)

    def _check_idle(self):
        if self.change_x == 0 and self._is_attacking == False:
            self._is_walking = False 
            self._current_frame += 1
            if self._current_frame >= constants.PLAYER_ANIMATION_RATE:
                num_textures = len(constants.get_texture("PLAYER_IDLE"))
                self._current_frame = 0
                self._texture_index = (self._texture_index + 1) % num_textures
                self.texture = constants.get_texture("PLAYER_IDLE", self.facing_left)[self._texture_index]

    def _check_walking(self):
        if self.change_x != 0 and not self._is_jumping:
            self._current_frame += 1
            if self._current_frame >= constants.PLAYER_ANIMATION_RATE:
                num_textures = len(constants.get_texture("PLAYER_WALKING"))
                self._current_frame = 0
                self._texture_index = (self._texture_index + 1) % num_textures
                self.texture = constants.get_texture("PLAYER_WALKING", self.facing_left)[self._texture_index]

    def _check_attacking(self):
        if self._is_attacking == True:
            self._current_frame += 1
            if self._current_frame >= constants.PLAYER_ANIMATION_RATE:
                if self._texture_index == len(constants.ATTACK1) - 2:
                    self._is_attacking = False
                num_textures = len(constants.ATTACK1)
                self._current_frame = 0
                self._texture_index = (self._texture_index + 1) % num_textures
                self.texture = constants.ATTACK1[self._texture_index]

    def _draw_health_bar(self):
        """ Draw the health bar """

        # Draw the 'unhealthy' background
        if self.current_health < self.max_health:
            arcade.draw_rectangle_filled(center_x=self.center_x,
                                         center_y=self.center_y + constants.HEALTHBAR_OFFSET_Y,
                                         width=constants.HEALTHBAR_WIDTH,
                                         height=3,
                                         color=arcade.color.RED)

        # Calculate width based on health
        health_width = constants.HEALTHBAR_WIDTH * (self.cur_health / self.max_health)

        arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (constants.HEALTHBAR_WIDTH - health_width),
                                     center_y=self.center_y - 10,
                                     width=health_width,
                                     height=constants.HEALTHBAR_HEIGHT,
                                     color=arcade.color.GREEN)
   
    def _update_position(self):
        self.change_y -= constants.GRAVITY   
        self.center_y += self.change_y
        self.center_x += self.change_x