import random
import json
from pathlib import Path

import os

class Flavor_Text():
    def __init__(self, flavor_type, flavor_index):
        self.flavor_type = flavor_type
        self.flavor_index = flavor_index
    
    def get_flavor(self)
        json_filepath = str(Path(os.path.dirname(__file__)).parents[0]) + "/_json/flavor.json"
        
        with open(json_filepath) as f
            data = json.load(f)
    
class Flavor_Boom(Flavor_Text):
    def __init__(self, result):
        super().__init__(