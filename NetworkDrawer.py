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

    @staticmethod
    def get_network_useage_table(cap):
        """Run tshark to decode and display the packet. If no args defined uses -V"""
        f = open("temp.txt", "w")
        subprocess.call(["tshark", "-nr", cap, "-z", "conv,ip", "-q"], stdout=f)
        f.close()
        f = open("temp.txt", "r")
        output = f.read()
        f.close()
        remove("temp.txt")
        return output

    def get_expert_info(cap):
        """ returns a retransmission rate and other analysis information """
        f = open("temp.txt", "w")
        subprocess.call(["tshark", "-nr", cap, "-z", "expert", "-q"], stdout=f)
        f.close()
        f = open("temp.txt", "r")
        output = f.read()
        f.close()
        remove("temp.txt")
        return output

    def get_load_measure(cap, Interval):
        """ returns a loading rate (interval / frame / bytes) """
        f = open("temp.txt", "w")
        subprocess.call(["tshark", "-o", "tcp.desegment_tcp_streams:FALSE" ,"-n", "-q" , "-r", cap, "-z", "io,stat," + Interval + ",,FRAMES,BYTES"], stdout=f)
        f.close()
        f = open("temp.txt", "r")
        output = f.read()
        f.close()
        remove("temp.txt")
        return output

    def get_traffic_for_ip_in_time(cap, ip, time):
        """ tshark -r filename.cap -Y "(frame.time >= \"2016-12-25 09:15:43\") && ip.addr == 255.255.255.255" """
        f = open("temp.txt", "w")
        subprocess.call(["tshark", "-r", cap, "-Y", "(frame.time >= \"" + time + "\") && ip.addr == " + ip], stdout=f)
        f.close()
        f = open("temp.txt", "r")
        output = f.read()
        f.close()
        remove("temp.txt")
        return output