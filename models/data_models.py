from typing import List

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def as_dict(self):
        d = {"x" : self.x,
             "y" : self.y}

        return d

class Attack:
    def __init__(self, block_id: str, target: Point):
        self.block_id = block_id
        self.target = target
    def as_dict(self):
        d = {"build_id" : self.block_id,
             "target" : self.target.as_dict()}
        
        return d

class StepData:
    def __init__(self, attacks: List[Attack], builds: List[Point], base_pos: Point):
        self.attacks = attacks
        self.builds = builds
        self.base_pos = base_pos
    def as_dict(self):
        d = {"attacks" : [x.as_dict() for x in self.attacks],
             "builds" : [x.as_dict() for x in self.builds],
             "base_pos" : self.base_pos.as_dict()}
        
        return d
