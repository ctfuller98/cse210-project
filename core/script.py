from collections import defaultdict


class Script:

    def __init__(self):
        self._current_actions = defaultdict(list)
        self._removed_actions = defaultdict(list)
        
    def add_action(self, cue_name, action):
        self._current_actions[cue_name].append(action)
        
    def clean_actions(self):
        for cue_name in self._removed:
            current = set(self._current_actions[cue_name])
            removed = set(self._removed_actions[cue_name])
            self._current_actions[cue_name] = list(current - removed)
        self._removed_actions.clear()
            
    def get_actions(self, cue_name):
        return self._current_actions.get(cue_name, list())

    def remove_action(self, cue_name, action):
        self._removed_actions[cue_name].append(action)