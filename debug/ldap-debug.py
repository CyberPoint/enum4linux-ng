#!/usr/bin/env python3

import sys
import pprint
from ldap3 import Server, Connection, DSA
#from ldap3.core.exceptions import LDAPSocketOpenError

def get_namingcontexts(host, tls):
    try:
        server = Server(host, use_ssl=tls, get_info=DSA, connect_timeout=2)
        ldap_con = Connection(server, auto_bind=True)
        ldap_con.unbind()
    except Exception as e:
        pprint.PrettyPrinter().pprint(e.args)
        error = str(e.args[1][0][0])
        if "]" in error:
            error = error.split(']', 1)[1]
        elif ":" in error:
            error = error.split(':', 1)[1]
        error = error.lstrip().rstrip()

        print(error)

if not len(sys.argv) > 1:
    print(f"Usage: {sys.argv[0]} host")
    sys.exit(1)

host = sys.argv[1]
get_namingcontexts(host,True)
get_namingcontexts(host,False)
