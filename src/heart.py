#!usr/bin/python

from subsystem import Subsystem

class Heart(Subsystem):
    def __init__(self, name, freq):
        self.name = name
        self.freq = freq
    
    def start(self, t=20):
        """On start() the heart will have t seconds until kill w/o controller inputs"""
        pass

    def kill(self):
        #TODO override
        pass

    def send(self):
        # sends a frequency in bpm
        pass

    def receive(self):
        # receives hormones "epi-10"; "ace-06"
        self.update_freq('ace', '10')
        pass

    def update_freq(self, type, qty):
        """
        Update beat frequency based on hormone types and quantity inputs
        """
        # if ace then -- by qty
        # if epi then ++ by qty
        new_freq = 0
        self.freq = new_freq

if __name__ == '__main__':
    heart = Heart("heart")
    #TODO
    heart.start(t=20)