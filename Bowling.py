from Frame import FrameIterator

class Bowling:
    def __init__(self, scores):
        self.__rolls = Bowling.__calculate(scores)
       
    @staticmethod 
    def __calculate(scores):
        rolls = [0]*len(scores)
        for i in range(len(scores)):
            if scores[i] == 'X':
                rolls[i] = 10
            elif scores[i] == '/':
                rolls[i] = 10 - rolls[i-1]
            elif scores[i] == '-':
                rolls[i] = 0
            else:
                rolls[i] = int(scores[i])
        return rolls
            
    def score(self):
        frames = FrameIterator(self.__rolls)
        summary = 0
        while not frames.isDone():
            frame = frames.currentItem()
            summary += frame.score()
            frames.next() 
        return summary
