blocked_countries = ["CN", "RU", "KP"]

def geo_check(country):
    return country not in blocked_countries
