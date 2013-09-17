class FrameIterator:
    def __init__(self, rolls):
        self.__NumberOfRoll = len(rolls)
        self.__rolls = rolls + [0]
        self.__start_pos = 0
        self.__end_pos = 0
        self.__step = 0
        
    def first(self):
        self.__start_pos = 0
        
    def next(self):
        self.__start_pos += self.__step
    
    def isDone(self):
        return self.__end_pos == self.__NumberOfRoll
    
    def currentItem(self):
        frame = self.__createFrame()
        self.__end_pos = self.__start_pos + frame.length()
        self.__step = frame.step()
        return frame
    
    def __createFrame(self):
        MaxNumberOfEffectedRoll = 3
        frame_rolls = self.__rolls[self.__start_pos:self.__start_pos+MaxNumberOfEffectedRoll]
        if frame_rolls[0] == 10:
            return Strike(frame_rolls[1:3])
        elif frame_rolls[0] + frame_rolls[1] == 10:
            return Spare(frame_rolls[2])
        else:
            return NormalFrame(frame_rolls[:2])

class Strike:
    def __init__(self, rolls):
        self.__extra_rolls = rolls
    
    def score(self):
        result = 10
        for roll in self.__extra_rolls:
            result += roll
        return result
    
    def step(self):
        return 1
    
    def length(self):
        return 3
        

class Spare:
    def __init__(self, roll):
        self.__extra_roll = roll
        
    
    def score(self):
        return 10 + self.__extra_roll
    
    def step(self):
        return 2
    
    def length(self):
        return 3
    
class NormalFrame:
    def __init__(self, rolls):
        self.__rolls = rolls
        
    def score(self):
        result = 0
        for roll in self.__rolls:
            result += roll
        return result
    
    def step(self):
        return 2
    
    def length(self):
        return 2