# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 08:39:41 2015

@author: Agustina  Arroyuelo
"""
def int_to_time(seconds):
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time
        
class Time(object):
    def print_time(self):
        print ('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
        
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
        
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    
    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
        
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

start=Time()
start.hour=4
start.minute=55
start.second=15
        
start.print_time()
end = start.increment(1337)
end.print_time()
print end.is_after(start)
lala=start+end
lala.print_time()
