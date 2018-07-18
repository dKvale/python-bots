import random
import sc2
from math import fabs
from sc2 import run_game, maps, Race, Difficulty
from sc2.position import Point2
from sc2.constants import *
from sc2.player import Bot, Computer, Human
from sc2.helpers import ControlGroup


class workerRush2(sc2.BotAI):

    async def on_step(self, iteration):
      
        def select_target(self):
              
            target = self.known_enemy_units
            if target.exists:
                return target.random.position

            if min([u.position.distance_to(self.enemy_start_locations[0]) for u in self.units]) < 2:
              
                target = self.known_enemy_structures
                if target.exists:
                    return target.random.position
                  
                return self.enemy_start_locations[0].position

            return self.state.mineral_field.random.position
      
        for worker in self.workers:
            target = self.select_target()
            await self.do(worker.attack(target))
            
        if self.can_afford(SCV) and self.workers.amount < 22 and cc.noqueue:
            await self.do(cc.train(SCV))
