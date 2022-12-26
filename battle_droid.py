from droid import SeparatistDroid


class BattleDroid(SeparatistDroid):
    MAX_FIREPOWER = 100
    DAMAGE = 1

    def __init__(self, legion, date_manufactured):
        super().__init__(max_firepower=self.MAX_FIREPOWER, damage=self.DAMAGE, legion=legion, \
                         date_manufactured=date_manufactured)

    def __repr__(self):
        return 'battle droid'
