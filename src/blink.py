#!usr/bin/python

class Blink():
    def __init__(self, name, freq=60):
        self.name = name
        self.freq = freq
    
    def start(self, t=20):
        pass

    def kill(self):
        #TODO override
        pass

    def send(self):
        # sends a frequency in bpm
        pass

    def receive(self):
        self.update_freq('0000010101011111101')
        pass

    def update_freq(self, package):
        """
        Update beat frequency based on hormone types and quantity inputs
        """
        new_freq = 0
        self.freq = new_freq

if __name__ == '__main__':
    blink = Blink("blink")
    blink.start()