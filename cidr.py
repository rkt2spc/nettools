#!/usr/bin/env python

import ipaddress
import argparse

parser = argparse.ArgumentParser(description='CIDR subnet splitting utilities.', formatter_class=argparse.MetavarTypeHelpFormatter)
parser.add_argument('--cidr', type=str, required=True, help='IPv4 CIDR block of the parent network (i.e 10.0.0.0/16).')
parser.add_argument('--bits', type=int, required=True, help='Number of bits added to parent netmask to create each subnets.')

args = parser.parse_args()

net = ipaddress.IPv4Network(args.cidr, strict=True)
subnets = list(net.subnets(prefixlen_diff=args.bits))

print("Network:")
print(net)
print()
print("Subnets:")
for sn in subnets:
    print(sn)