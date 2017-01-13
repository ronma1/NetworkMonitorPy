import networkx as nx
import matplotlib.pyplot as plt
from scapy.all import *

"""
NetworkDrawer 
Implement here all graphical functionallity regard to the assignment
(Not include GUI here)
"""
class NetworkDrawer:

    @staticmethod
    def draw_network(network):
        pos=nx.fruchterman_reingold_layout(network, k=400)
        nx.draw(network, pos, edge_color='#A0CBE2', with_labels = True, node_size=200, node_color='r', font_size=12)  # networkx draw()
        plt.draw()  # pyplot draw()
        plt.show()

    @staticmethod
    def pdfdump(pkt, filename='default.pdf'):
        pkt.pdfdump(filename)
        
    @staticmethod
    def print_pkt_decoder(pkt):
        t= tdecode(pkt)
        print (t)
