def analyze_packet(packet):
    threats = ["sql", "xss", "malware"]
    for t in threats:
        if t in packet.lower():
            return "INTRUSION DETECTED"
    return "SAFE"
