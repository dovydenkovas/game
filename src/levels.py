class levels:
    def __init__(self, title, map, entites, background_frames, background_current_index):
        self.title = title
        self.map = map
        self.entites = entites
        self.background_frames = background_frames
        self.background_current_index = background_current_index

    def run(self):
        '''draw run'''
        pass

    def draw(self):
        '''draw'''
        pass

    def begin(self):
        '''begin'''
        pass

    def check_end(self):
        '''check_end'''
        pass

    def check_over(self):
        '''check_over'''
        pass

    def generate_entites(self):
        '''generate entites'''
        pass

class lvl_1(levels):
    def __init__(self):
        super(lvl_1, self).__init__()

class lvl_2(levels):
    def __init__(self):
        super(lvl_2, self).__init__()

class lvl_3(levels):
    def __init__(self):
        super(lvl_3, self).__init__()

class lvl_4(levels):
    def __init__(self):
        super(lvl_4, self).__init__()