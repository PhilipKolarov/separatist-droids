from abc import abstractmethod, ABC
from time import sleep


class SeparatistDroid (ABC):
    RELOAD_COMPLETE_MESSAGE = 'You have reached the maximum firepower capacity'
    SLEEP_TIME = 0.1
    MAX_HEALTH = 30

    def __init__(self, max_firepower, damage, legion, date_manufactured):
        self.kills = 0
        self._max_firepower = max_firepower
        self.firepower = max_firepower
        self.damage = damage
        self._max_health = self.MAX_HEALTH
        self.health = self.MAX_HEALTH
        self.legion = legion
        self.date_manufactured = date_manufactured

    def shoot(self):
        self.firepower -= 1

    def reload(self):
        while self.firepower != self._max_firepower:
            self.firepower += 1
            sleep(0.1)
        return self.RELOAD_COMPLETE_MESSAGE

    def hit(self, attacker):
        self.health -= attacker.DAMAGE
        if self.health <= 0:
            self.__del__()

    def __del__(self):
        print(f"{self.__repr__()} has been destroyed")
