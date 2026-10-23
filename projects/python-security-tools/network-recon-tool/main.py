from pathlib import Path

from modules.dns_enum import enumerate_subdomains
from modules.port_scan import scan_hosts
from modules.reporting import save_report


DEFAULT_PORTS = [22, 53, 80, 443, 445, 3389]


def main():
    print("Python Network Reconnaissance Tool")
    print("Use only against systems you own or are authorized to test.\n")

    domain = input("Target domain: ").strip()
    dns_server = input("DNS server [8.8.8.8]: ").strip() or "8.8.8.8"

    wordlist = Path(__file__).parent / "data" / "subdomains.txt"

    dns_results = enumerate_subdomains(
        domain=domain,
        wordlist=wordlist,
        dns_server=dns_server,
    )

    hosts = sorted({ip for item in dns_results for ip in item["addresses"]})

    if not hosts:
        print("\nNo hosts were discovered, so the port scan was skipped.")
        scan_results = []
    else:
        print(f"\nDiscovered {len(hosts)} unique IP address(es).")
        print(f"Scanning selected ports: {DEFAULT_PORTS}\n")
        scan_results = scan_hosts(hosts, DEFAULT_PORTS)

    report_path = save_report(
        domain=domain,
        dns_server=dns_server,
        dns_results=dns_results,
        scan_results=scan_results,
    )

    print(f"\nReport saved to: {report_path}")


if __name__ == "__main__":
    main()
