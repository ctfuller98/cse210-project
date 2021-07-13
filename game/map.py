import arcade

class Map():
    
    def __init__(self, map_name, scene):
        
        # Name of the layer in the file that has our platforms/walls
        platforms_layer_name = 'Platforms'

        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        # -- Platforms
        self._platforms = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=platforms_layer_name,
                                                      scaling=1,
                                                      use_spatial_hash=True)
        for tile in self._platforms:
            scene.get_cast().add_actor("grounds", tile)

        scene.get_cast().add_actor("map", self)

    def draw(self):
        for tile in self._platforms:
            tile.draw()
             