import random
class Artefact:
    def __init__(self, name, attack_buff, defense_buff, speed_buff, spawn_chance, reloading_buff, texture_icon, texture_on_floor, texture_in_use):
        self.attack_buff = attack_buff
        self.defense_buff = defense_buff
        self.speed_buff = speed_buff
        self.spawn_chance = spawn_chance
        self.reloading_buff = reloading_buff
        self.name = name
        self.texture_icon = texture_icon
        self.texture_on_floor = texture_on_floor
        self.texture_in_use = texture_in_use
    def draw(self):
        ''' draw'''
        pass

class sword(Artefact):
    def __init__(self):
        super(sword, self).__init__('sword', 10, random.randint(1,5), -0.5, 10, 3)

class shield(Artefact):
    def __init__(self):
        super(shield, self).__init__('shield', 1, 10,-0.5, 10, 0)

class fur_coat(Artefact):
    def __init__(self):
        super(fur_coat, self).__init__('fur_coat', 0, 10, -1, 15, 0)

class felt_boot(Artefact):
    def __init__(self):
        super(felt_boot, self).__init__('felt_boot', 0, 8, 2, 10, 0)

class mittens(Artefact):
    def __init__(self):
        super(mittens, self).__init__('mittens', 0, 3, 0, 15, 0)

class hat_with_ear_flaps(Artefact):
    def __init__(self):
        super(hat_with_ear_flaps, self).__init__('hat_with_ear_flaps', 0, 3, 0, 15, 0)

class shovel(Artefact):
    def __init__(self):
        super(shovel, self).__init__('shovel', 5, random.randint(1,5), -1, 25, 2)