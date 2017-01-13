from scapy.all import *
import networkx as nx
from NetworkDrawer import NetworkDrawer

# PcapReader
# Denotes a basic interface againts a specific given cap file
class PcapReader:
    
    def __init__(self, cap_path):
        self.cap_path = cap_path
        self.pcap = rdpcap(self.cap_path)
        self.graph = self.generate_network_graph()

    # getByLayer
    # return a list of packets by layer
    def getByLayer(self, layer=Dot11):
        pkts = [] # 802.11 pkts
        for pkt in self.pcap:
            if pkt.haslayer(layer):
                pkts.append(pkt)

        return pkts

    # generate_network_graph
    # genereates an network graph of the given pcap
    def generate_network_graph(self):
        self.G = nx.Graph()
        self.ip_pkts = self.getByLayer('IP')
        for pkt in self.ip_pkts:
            self.G.add_edge(pkt.src, pkt.dst)
        return self.G

    # show_network
    # shows the network graph of the given pcap
    def show_network(self):
        NetworkDrawer.draw_network(self.graph)

    # pkt_by_ip
    # returns a list of packets by specific ip
    def pkt_by_ip(self, ip=None):
        is_Error = False
        if ip is None:
            print('ip address mush be specified.')
            return None

        pkts_by_ip = []

        for pkt in self.ip_pkts:
            if pkt.src == ip or pkt.dst == ip:
                pkts_by_ip.append(pkt)

        return pkts_by_ip

    # single_ip_graph
    # creates a network from a given packet list
    def single_ip_graph(self, pkt_by_ip):
        G = nx.Graph()
        for pkt in pkt_by_ip:
            G.add_edge(pkt.src, pkt.dst)
        return G
