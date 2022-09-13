def ip_to_host(addr):
    """ convert an IP address to a host name, returning shortname and fqdn to the 
        caller
    """

    try:
        fqdn = socket.gethostbyaddr(addr)[0]
        shortname = fqdn.split('.')[0]
        if fqdn == shortname:
            fqdn = ""

    except:
        # can't resolve it, so default to the address given
        shortname = addr
        fqdn = ""

    return shortname, fqdn 

ip_to_host(192.168.174.250)
