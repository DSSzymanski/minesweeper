import time
import math

class Stopwatch():
    def __init__(self):
        self.start_time = None
        self.end_time = None
        
    def get_time(self):
        if self.start_time != None:
            if self.end_time != None:
                return str(int(math.floor(self.end_time - self.start_time)))
            else:
                return str(int(math.floor(time.time() - self.start_time)))
        else: 
            return "0"
    
    def draw_timer(self):
        fill(0)
        textSize(32)
        text(str(self.get_time()), 15*width/16, height/16 - 12)
        fill(220, 220, 220)
        
        return self.get_time()
    
    def start(self):
        if self.start_time == None:
            self.start_time = time.time()
        
    def stop(self):
        self.end_time = time.time()
        
    def reset(self):
        self.start_time, self.end_time = None, None
