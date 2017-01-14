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
    print('[8] ' + 'Get a network useage table (Exported by ip from tshark)')
    print('[9] ' + 'Get retransmissions (PER) and expert info (PIPE from tshark command)')
    print('[10] ' + 'Get loading measurement Frames/Bytes per pcap interval (PIPE from tshark command)')
    print('[11] ' + 'Get traffic from/to specific ip from specific time (PIPE from tshark command)')
    print('[0] ' + 'exit')
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
    elif 8 == selected:
        output = NetworkDrawer.get_network_useage_table(reader.cap_path)
        print(output)
    elif 9 == selected:
        output = NetworkDrawer.get_expert_info(reader.cap_path)
        print(output)
    elif 10 == selected:
        interval = input("Insert the Interval (default full packet): ")
        if interval == "":
            interval = "0"
        output = NetworkDrawer.get_load_measure(reader.cap_path,interval)
        print(output)
    elif 11 == selected:
        ip = input("Please enter ip(example: 255.255.255.255) to look up: ")
        time = input("Please enter time(Must follow the format: 2016-12-25 09:15:43): ")
        output = NetworkDrawer.get_traffic_for_ip_in_time(reader.cap_path, ip, time)
        print(output)
    elif 0 == selected: 
        sys.exit()
    else:
        print('Invalid options! ')
    

if __name__ == '__main__':
    main(sys.argv[1:])