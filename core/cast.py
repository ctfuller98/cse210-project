from collections import defaultdict
from itertools import chain


class Cast:

    def __init__(self):
        super().__init__()
        self._current_actors = defaultdict(list)
        self._removed_actors = defaultdict(list)
        
    def add_actor(self, group, actor):
        self._current_actors[group].append(actor)
        
    def clean_actors(self):
        for group in self._removed_actors:
            current = set(self._current_actors[group])
            removed = set(self._removed_actors[group])
            self._current_actors[group] = list(current - removed)
        self._removed_actors.clear()

    def first_actor(self, group):
        actors = self._current_actors.get(group, list())
        if (len(actors) == 0):
            raise ValueError(f"there aren't any actors in {group}")
        return actors[0]

    def get_actors(self, group):
        return self._current_actors.get(group, list())

    def remove_actor(self, group, actor):
        self._removed_actors[group].append(actor)