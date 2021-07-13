import arcade
from game import constants, player
import timeit
class Map():
    
    def __init__(self, map_name, scene):
        self.update_every_other_frame = 0
        self.scroll_x = 0
        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)
        self._background_images = list()
        for i in range(3):
            self._background_images.append(arcade.load_texture(constants.PROJECT_ROOT + f"/assets/maps/forest_01/bg_{i}.png"))
        
        self._center_tile = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name="Center",
                                                      scaling=1,
                                                      use_spatial_hash=True)
        print(self._center_tile[0].center_x)
        self._background = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name="Background",
                                                      scaling=1,
                                                      use_spatial_hash=True)

        # -- Platforms
        self._platforms = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name="Platforms",
                                                      scaling=1,
                                                      use_spatial_hash=True)
        for tile in self._platforms:
            scene.get_cast().add_actor("grounds", tile)

        self._scene = scene

        scene.get_cast().add_actor("map", self)

    def draw(self):
        
        start_time = timeit.default_timer()

        players = self._scene.get_cast().get_actors("players")
        self.scroll_x = (players[0].center_x + players[1].center_x) // 2 - constants.SCREEN_WIDTH // 2
        
        self.scroll_y =  (players[0].center_y + players[1].center_y) // 2 - constants.SCREEN_HEIGHT // 2
        self.scroll_y = max(0, self.scroll_y)
        self.scroll_x = max(0, self.scroll_x)
        self.scroll_x = min(208, self.scroll_x)
        
        arcade.set_viewport(self.scroll_x, self.scroll_x + constants.SCREEN_WIDTH, self.scroll_y ,self.scroll_y + constants.SCREEN_HEIGHT)
        

        x_ratio = self.scroll_x / 208
        x_ratio -= 0.5

        arcade.draw_lrwh_rectangle_textured(self.scroll_x , self.scroll_y , constants.SCREEN_WIDTH , constants.SCREEN_HEIGHT , self._background_images[0])
        arcade.draw_lrwh_rectangle_textured(self.scroll_x + (constants.SCREEN_WIDTH * 0.02 * x_ratio) - constants.SCREEN_WIDTH * 0.02, self.scroll_y , constants.SCREEN_WIDTH * 1.05 , constants.SCREEN_HEIGHT , self._background_images[1])
        arcade.draw_lrwh_rectangle_textured(self.scroll_x + (constants.SCREEN_WIDTH * 0.03 * x_ratio) - constants.SCREEN_WIDTH * 0.03, self.scroll_y , constants.SCREEN_WIDTH * 1.06 , constants.SCREEN_HEIGHT , self._background_images[2])

        self._background.draw()
        self._platforms.draw())