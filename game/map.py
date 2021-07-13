import arcade

class Map():
    
    def __init__(self, map_name, scene):
        

        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        
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

        scene.get_cast().add_actor("map", self)

    def draw(self):
        for tile in self._background:
            tile.draw()
        for tile in self._platforms:
            tile.draw()
             