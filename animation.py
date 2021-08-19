class RepeatException(Exception):
    def __init__(self):
        super().__init__("First frame cannot be _n")

class Animation:
    """ Animation Class.
        To repeat a frame, give '_n' as the frame after with n = number of repetitions
        Arguments:
        -   frames: array containing executable strings. 
        -   dt: how many ticks per frame

        First frame cannot have _ as it's first character, as this signifies a repeat
    """
    def __init__(self, frames, dt):
        self.frames = frames 
        self.length = len(frames)
        self.dt = dt
        self.count = 0

        if frames[0][0] == '_':
            raise RepeatException

        self.repeat_count = 0

    def update(self, dt):
        if dt % self.dt == 0:
            if self.count < self.length - 1:
                next_frame = self.count + 1
            else:
                next_frame = 0

            if self.frames[next_frame][0] == '_':
                if self.repeat_count < int(self.frames[next_frame][1:]):
                    self.repeat_count += 1
                else:
                    self.count += 1
                    self.repeat_count = 0
            else:
                self.count += 1

            try:
                if self.frames[self.count][0] == '_':
                    if self.count < self.length - 1:
                        self.count += 1
                    else:
                        self.count = 0
            except Exception as e:
                pass

            if self.count > self.length - 1:
                self.count = 0

            return self.frames[self.count]
        else:
            return 'None'