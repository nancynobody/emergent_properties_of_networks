#!usr/bin/python

# TODO 
# TEST SEND/RCV UDP PACKETS BACK AND FORTH B/T 2 SUBSYSTEMS
# .... 3 SUBSYSTEMS

import socket
import threading

class Subsystem():
    
    def __init__(self, name, host, port):
        self.name = name
        self.native_address = ("", 7788)
        self.known_subsystems = [(ip, port), (ip, port), (ip, port)]
        
        # Create a socket (AF_INET => network oriented, UDP name => sock _DGRAM)
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind the native ip and port ("" => local ip)
        udp_socket.bind(self.native_address)

        # Specify the ip and port of the others
        # for subsys in self.known_subsystems:  #NEED 2 THREADS FOR EACH SUBSYSTEM
        dest_ip = ""
        dest_port = 12345

        # Create a thread and run it (args => tuples)
        ts = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))
        tr = threading.Thread(target=recv_msg, args=(udp_socket,))
        
        ts.start()
        tr.start()


    def start(self):
        pass

    def kill(self):
        pass

    def send(self, udp_socket, dest_ip, dest_port):
        """Send data from current subsystem to another one"""
        #  gets the content to send 
        while True:
            send_data = input(" please enter a message to send ：")
            udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))


    def recv_msg(self, udp_socket,):
        """Receive data from another subsystem to current one"""
        while True:
            recv_data = udp_socket.recvfrom(1024)
            print("\n got the message %s:%s" % (str(recv_data[1]), recv_data[0].decode("gbk")))

if __name__ == '__main__':
    subsystem = Subsystem("A", "", '12345')