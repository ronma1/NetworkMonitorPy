import networkx as nx
import matplotlib.pyplot as plt
from scapy.all import *
from os import remove

"""
NetworkDrawer 
Implement here all graphical functionallity regard to the assignment
(Not include GUI here)
"""
class NetworkDrawer:

    @staticmethod
    def draw_network(network):
        """ draws a given network represented as networkx graph """
        pos=nx.fruchterman_reingold_layout(network, k=400)
        nx.draw(network, pos, edge_color='#A0CBE2', with_labels = True, node_size=200, node_color='r', font_size=12)  # networkx draw()
        plt.draw()  # pyplot draw()
        plt.show()

    @staticmethod
    def pdfdump(pkt, filename='default.pdf'):
        """ uses scapy pdfdump command """
        pkt.pdfdump(filename)
        
    @staticmethod
    def print_pkt_decoder(pkt):
        """Run tshark to decode and display the packet. If no args defined uses -V"""
        fname = get_temp_file()
        wrpcap(fname,[pkt])
        f = open("temp.txt", "w")
        subprocess.call(["tshark", "-r", fname, "-V"], stdout=f)
        f.close()
        f = open("temp.txt", "r")
        output = f.read()
        f.close()
        remove("temp.txt")
        return output

    @staticmethod
    def open_in_wireshark(pktlist):
        """Run wireshark on a list of packets"""
        fname = get_temp_file()
        wrpcap(fname, pktlist)
        subprocess.call([conf.prog.wireshark, "-r", fname])

