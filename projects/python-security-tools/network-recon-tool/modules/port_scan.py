from scapy.all import IP, TCP, send, sr1


def scan_host(host, ports):
    findings = []

    for port in ports:
        packet = IP(dst=host) / TCP(dport=port, flags="S")
        response = sr1(packet, timeout=1, verbose=0)

        if response is None:
            state = "filtered/no response"
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            state = "open"
            send(IP(dst=host) / TCP(dport=port, flags="R"), verbose=0)
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
            state = "closed"
        else:
            state = "unknown"

        print(f"[TCP] {host}:{port} -> {state}")
        findings.append({"host": host, "port": port, "state": state})

    return findings


def scan_hosts(hosts, ports):
    results = []
    for host in hosts:
        results.extend(scan_host(host, ports))
    return results
