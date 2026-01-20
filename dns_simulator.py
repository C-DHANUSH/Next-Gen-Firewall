blocked_sites = set()

def block_site(site):
    blocked_sites.add(site)

def unblock_site(site):
    blocked_sites.discard(site)

def is_blocked(site):
    return site in blocked_sites
