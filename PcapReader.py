from scapy.all import rdpcap, Dot11
import networkx as nx
from NetworkDrawer import NetworkDrawer

class PcapReader:
    """ 
        class : PcapReader
        Denotes a basic interface againts a specific given cap file
    """
    
    def __init__(self, cap_path):
        self.cap_path = cap_path
        self.pcap = rdpcap(self.cap_path)
        self.graph = self.generate_network_graph()

    def getByLayer(self, layer=Dot11):
        """
            getByLayer
            return a list of packets by layer
        """
        pkts = [] # 802.11 pkts
        for pkt in self.pcap:
            if pkt.haslayer(layer):
                pkts.append(pkt)

        return pkts

    def generate_network_graph(self):
        """
            generate_network_graph
            genereates an network graph of the given pcap
        """
        self.G = nx.Graph()
        self.ip_pkts = self.getByLayer('IP')
        for pkt in self.ip_pkts:
            self.G.add_edge(pkt.src, pkt.dst)
        return self.G

    def show_network(self):
        """
            show_network
            shows the network graph of the given pcap
        """
        NetworkDrawer.draw_network(self.graph)

    def pkt_by_ip(self, ip=None):
        """
            pkt_by_ip
            returns a list of packets by specific ip
        """
        is_Error = False
        if ip is None:
            print('ip address mush be specified.')
            return None

        pkts_by_ip = []

        for pkt in self.ip_pkts:
            if pkt.src == ip or pkt.dst == ip:
                pkts_by_ip.append(pkt)

        return pkts_by_ip

    def single_ip_graph(self, pkt_by_ip):
        """
            single_ip_graph
            creates a network from a given packet list
        """
        G = nx.Graph()
        for pkt in pkt_by_ip:
            G.add_edge(pkt.src, pkt.dst)
        return G

    def nodes_quantity(self):
        """
            nodesQuantity
            returns the number of nodes in the network's graph
        """
        return nx.number_of_nodes(self.graph)

    def get_ip_list(self):
        """ returns a list of the ips in the graph """
        return self.graph.nodes()
