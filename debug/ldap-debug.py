#!/usr/bin/env python3

import sys
import pprint
from ldap3 import Server, Connection, DSA

def get_namingcontexts(host, tls):
    try:
        server = Server(host, use_ssl=tls, get_info=DSA, connect_timeout=2)
        ldap_con = Connection(server, auto_bind=True)
        ldap_con.unbind()
    except Exception as e:
        pprint.PrettyPrinter().pprint(e.args)

if not len(sys.argv) > 1:
    print(f"Usage: {sys.argv[0]} host")
    sys.exit(1)

host = sys.argv[1]
get_namingcontexts(host,True)
get_namingcontexts(host,False)

