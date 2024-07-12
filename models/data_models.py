from typing import List

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Attack:
    def __init__(self, build_id: str, target: Point):
        self.build_id = build_id
        self.target = target

class StepData:
    def __init__(self, attacks: List[Attack], builds: List[Point], base_pos: Point):
        self.attacks = attacks
        self.builds = builds
        self.base_pos = base_pos