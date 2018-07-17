import random
import sc2
from math import fabs
from sc2 import run_game, maps, Race, Difficulty
from sc2.position import Point2
from sc2.constants import *
from sc2.player import Bot, Computer, Human
from sc2.helpers import ControlGroup


class workerRushBot(sc2.BotAI):
