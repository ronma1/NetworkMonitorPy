# from PcapReader import PcapReader
# import networkx as nx
# from NetworkDrawer import NetworkDrawer


#######################
#   Main for tests    #
#######################

# if __name__ == '__main__':
#     reader = PcapReader('test-data/android-Sun-Dec-25-10-42-29-GMT+02-00-2016.cap')
#     # ip_pkts = reader.pkt_by_ip('224.0.0.251')
#     # ip_Graph = reader.single_ip_graph(ip_pkts)
#     # NetworkDrawer.draw_network(ip_Graph)

#     # NetworkDrawer.pdfdump(reader.pcap[101], "mypacket.pdf")
#     # print "Number of nodes: " + str(reader.nodes_quantity())

#     # NetworkDrawer.open_in_wireshark(reader.pcap)
#     s = NetworkDrawer.get_traffic_for_ip_in_time(reader.cap_path, '255.255.255.255', '2016-12-25 09:15:43')
#     print()
#     print()
#     print(s)