from PcapReader import PcapReader
from NetworkDrawer import NetworkDrawer
import sys

global main_selections

def main(argv):
    """ runs the ui main loop """
    try:
        inputfile = argv[0]    
        reader = PcapReader(inputfile)  
        while True:
            selection = show_main_menu()
            handle_user_selection(selection, reader)
    except Exception as e:
        print(e)

def show_main_menu():
    """ 
        how menu + wait for user input 
        returns the user selection
    """ 
    print()
    print('[1] ' + 'Show network\'s relations graph')
    print('[2] ' + 'Show relations graph for specific IP')
    print('[3] ' + 'List the IPs in the network')
    print('[4] ' + 'Number of nodes in the network')
    print('[5] ' + 'Open in wireshark')
    print('[6] ' + 'Show specific packet information (from tshark interface)')
    print('[7] ' + 'Export specific packet to pdf (Scapy feature)')
    print('[9] ' + 'exit')
    print()
    selected = input('Your selection: ')
    return int(selected)

def handle_user_selection(selected, reader):
    print('===============================')
    if 1 == selected: 
        reader.show_network()
    elif 2 == selected:
        print('IP list: ')
        print(reader.get_ip_list())
        ip = input('Enter IP address: ')
        pkts_by_ip = reader.pkt_by_ip(ip)
        graph_ip = reader.single_ip_graph(pkts_by_ip)
        NetworkDrawer.draw_network(graph_ip)
    elif 3 == selected:
        print('IP list: ')
        print(reader.get_ip_list())
    elif 4 == selected:
        print('Number of nodes in the network\'s graph: ' + str(reader.nodes_quantity()))
    elif 5 == selected: 
        NetworkDrawer.open_in_wireshark(reader.pcap)
    elif 6 == selected:
        pkt_id = input('Select packet id: ')
        info = NetworkDrawer.print_pkt_decoder(reader.pcap[int(pkt_id)])
        print ("Packet " + str(pkt_id) + " info: ")
        print(info)
    elif 7 == selected:
        pkt_id = input('Select packet id: ')
        filename = input('Select the exported file\'s name: ')
        NetworkDrawer.pdfdump(reader.pcap[int(pkt_id)], str(filename))
    elif 9 == selected: 
        sys.exit()
    else:
        print('Invalid options! ')
    

if __name__ == '__main__':
    main(sys.argv[1:])