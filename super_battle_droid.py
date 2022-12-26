from separatist_droid import SeparatistDroid


class SuperBattleDroid(SeparatistDroid):
    MAX_FIREPOWER = 200
    DAMAGE = 2
    SLEEP_TIME = 0.05

    def __init__(self, legion, date_manufactured):
        super().__init__(max_firepower=self.MAX_FIREPOWER, damage=self.DAMAGE, legion=legion, \
                         date_manufactured=date_manufactured)

    def __repr__(self):
        return 'super battle droid'
