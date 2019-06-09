import time
import math

class Stopwatch():
    def __init__(self):
        self.start_time = None
        self.end_time = None
        
    def __str__(self):
        if self.start_time != None:
            if self.end_time != None:
                return str(int(math.floor(self.end_time - self.start_time)))
            else:
                return str(int(math.floor(time.time() - self.start_time)))
        else: 
            return "0"
        
    def __repr__(self):
        if self.start_time != None:
            if self.end_time != None:
                return str(int(math.floor(self.end_time - self.start_time)))
            else:
                return str(int(math.floor(time.time() - self.start_time)))
        else: 
            return "0"
    
    def start(self):
        if self.start_time == None:
            self.start_time = time.time()
        
        def stop(self):
        self.end_time = time.time()
        
    def reset(self):
        self.start_time, self.end_time = None, None
