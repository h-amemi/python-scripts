"""
Output ipaddresses

oneliner:
python3 -c "import ipaddress; [print(host) for host in ipaddress.ip_network('192.0.2.0/24').hosts()]"
"""

import argparse
import ipaddress


def main(ip_network):
    nw = ipaddress.ip_network(ip_network)
    for host in nw.hosts():
        print(host)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ip_network", help="CIDR notation. (e.g: 192.0.2.0/24)")
    args = parser.parse_args()
    main(args.ip_network)
