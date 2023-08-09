import random
import json
from pathlib import Path

import os

class Randomazzo():
    def __init__(self, flavor_type):
        self.flavor_type = flavor_type
    
    def get_flavor(self):
        json_filepath = str(Path(os.path.dirname(__file__)).parents[0]) + "/_json/flavor.json"
        
        with open(json_filepath) as f:
            data = json.load(f)
            flavor_text_array = random.choice(data[self.flavor_type])
            print(flavor_text_array)
            return flavor_text_array