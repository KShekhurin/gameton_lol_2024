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

class Base:
    def __init__(self, d : dict):
        self.attacks = d["attacks"]
        self.health = d["health"]
        self.id = d["id"]
        self.is_head = d["is_head"]
        self.last_attack = d["last_attack"]
        self.range = d["range"]
        self.x = d["x"]
        self.y = d["y"]

class EnemyBlock:
    def __init__(self, d : dict):
        self.attacks = d["attacks"]
        self.health = d["health"]
        self.is_head = d["is_head"]
        self.last_attack = d["last_attack"]
        self.name = d["name"]
        self.x = d["x"]
        self.y = d["y"]

class Player:
    def __init__(self, d : dict):
        self.enemy_block_kills = d["enemyBlockKills"]
        self.game_ended_at = d["gameEndedAt"]
        self.gold = d["gold"]
        self.name = d["name"]
        self.points = d["points"]
        self.zombie_kills = d["zombieKills"]

class Zombie:
    def __init__(self, d : dict):
        self.attack = d["attack"]
        self.direction = d["direction"]
        self.health = d["health"]
        self.id = d["id"]
        self.speed = d["speed"]
        self.type = d["type"]
        self.wait_turns = d["waitTurns"]
        self.x = d["x"]
        self.y = d["y"]

class ChangingData:
    def __init__(self, d : dict):
        self.base = [Base(x) for x in d["base"]]
        self.enemy_blocks = [EnemyBlock(x) for x in d["enemyBlocks"]]
        self.player = [Player(x) for x in d["player"]]
        self.real_name = d["realmName"]
        self.turn = d["turn"]
        self.turn_ends_in_ms = d["turnEndsInMs"]
        self.zombies = [Zombie(x) for x in d["zombies"]]


class ZPots:
    def __init__(self, d : dict):
        self.x = d["x"]
        self.y = d["y"]
        self.type = d["type"]

class NotChangingData:
    def __init__(self, d : dict):
        self.real_name = d["realmName"]
        self.zpots = [ZPots(x) for x in d["zpots"]]


class Round:
    def __init__(self, d : dict):
        self.duration = d["duration"]
        self.end_at = d["endAt"]
        self.name = d["name"]
        #self.repeat = d["repeat"]
        self.start_at = d["startAt"]
        self.status = d["status"]

class GameRounds:
    def __init__(self, d : dict):
        self.game_name = d["gameName"]
        self.now = d["now"]
        self.rounds = [Round(x) for x in d["rounds"]]


class ResponseToCommands:
    def __init__(self, d : dict):
        self.accepted_commands = [StepData(x) for x in d["acceptedCommands"]]
        self.errors = [x for x in d["errors"]]