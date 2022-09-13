def ip2name(addr):
    if not ip2name.resolve:
        return addr
    try:
        if addr in ip2name.cache:
            return ip2name.cache[addr]
        # FIXME: Workaround Python bug
        # Need double try/except to catch the bug
        try:
            name = gethostbyaddr(addr)[0]
        except KeyboardInterrupt:
            raise
    except (socket_host_error, ValueError):
        name = addr
    except (socket_host_error, KeyboardInterrupt, ValueError):
        ip2name.resolve = False
        name = addr
    ip2name.cache[addr] = name
    return name 

ip2name(str(192.168.174.250))
