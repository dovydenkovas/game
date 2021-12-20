class Entiry:
    def __intit__(self, health, defens, attack, speed, reloading, spawn_chance):
        self.health = health
        self.defens = defens
        self.attack = attack
        self.speed = speed
        self.reloading = reloading
        self.spawn_chance = spawn_chance

        def draw(self):

            pass


class Snowman(Entiry):
    def __init__(self):
        super(Snowman, self).__init__(10, 0, 30, 0, 2, 35)

    def move(self):
        pass

class Goblin(Entiry):
    def __intit__(self):
        super(Goblin, self).__intit__(10, 10, 10, 4, 1, 65)

    def move(self):
        pass

class TheGrinch(Entiry):
    def __intit__(self):
        super(TheGrinch, self).__intit__(100, 20, 30, 7, 5)
        
    def move(self):
        pass
